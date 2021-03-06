import numpy as np
import pulp
import itertools
from instance import Instance
from typing import List, Set, Dict
from logger import get_logger
import json
import encoder


def __generete_weekend_conmb(n_days: int) -> List[List[int]]:
    n = int(n_days/7)
    return [[j*7+6 if i & (1 << j) else j*7+5 for j in range(n)]
            for i in range(1 << n)]

# TODO add constraint name


def solve(instance: Instance):
    logger = get_logger(__name__)
    shiftids = [shift.id for shift in instance.shifts]
    staffids = [staff.id for staff in instance.staffs]
    n_days = instance.days
    n_staffs = len(instance.staffs)
    n_shifts = len(instance.shifts)
    weekend_combs = __generete_weekend_conmb(n_days)
    problem = pulp.LpProblem(name="scheduling", sense=pulp.LpMinimize)
    x = {(i, j, k): pulp.LpVariable(name='x_{}_{}_{}'.format(i, j, k), cat="Binary")
         for i, j, k in itertools.product(range(n_days), range(n_staffs), range(n_shifts))}

    t = {i: pulp.LpVariable(name='t_{}'.format(i), cat=pulp.LpInteger)
         for i in range(len(instance.section_covers))}

    # forbidden shift
    # This constraint always assumes that the last day of the previous planning period was a day off and the first day of the next planning horizon is a day off.
    for shift_idx in range(n_shifts):
        shift = instance.shifts[shift_idx]
        for forbidden_id, day, staff_idx in itertools.product(shift.forbidden, range(n_days), range(n_staffs)):
            if forbidden_id == '':
                continue
            forbidden_idx = shiftids.index(forbidden_id)
            if day == n_days-1:
                continue
            problem.addConstraint(
                x[day, staff_idx, shift_idx] + x[day+1, staff_idx, forbidden_idx] <= 1)

    # section cover
    for i in range(len(instance.section_covers)):
        section_cover = instance.section_covers[i]
        problem.objective += t[i]
        day = section_cover.day
        shift_idx = shiftids.index(section_cover.shift_id)
        problem.addConstraint(
            section_cover.weight_for_under*(section_cover.requirement -
                                            pulp.lpSum(x[day, staff_idx, shift_idx] for staff_idx in range(n_staffs))) <= t[i], name=f"section_cover_under_{day}_{shift_idx}")

        problem.addConstraint(
            section_cover.weight_for_over*(pulp.lpSum(x[day, staff_idx, shift_idx] for staff_idx in range(n_staffs))
                                           - section_cover.requirement) <= t[i], name=f"section_cover_over_{day}_{shift_idx}")

    # on_request
    for on_request in instance.on_requests:
        day = on_request.day
        staff_idx = staffids.index(on_request.staff_id)
        shift_idx = shiftids.index(on_request.shift_id)
        problem.objective += (1-x[day, staff_idx, shift_idx])*on_request.weight

    # off_request
    for off_request in instance.off_requests:
        day = off_request.day
        staff_idx = staffids.index(off_request.staff_id)
        shift_idx = shiftids.index(off_request.shift_id)
        problem.objective += x[day, staff_idx, shift_idx]*off_request.weight

    # days off
    for day_off in instance.days_off:
        staff_idx = staffids.index(day_off.staff_id)
        day = day_off.day
        for shift_idx in range(n_shifts):
            problem.addConstraint(
                x[day, staff_idx, shift_idx] >= 0, name=f"days_off_pos_{staff_idx}_{shift_idx}_{day}")
            problem.addConstraint(
                x[day, staff_idx, shift_idx] <= 0, name=f"days_off_neg_{staff_idx}_{shift_idx}_{day}")

    # section_staff
    for staff in instance.staffs:
        staff_idx = staffids.index(staff.id)
        # one shift for a day
        for day in range(n_days):
            problem.addConstraint(pulp.lpSum(
                x[day, staff_idx, shift_idx] for shift_idx in range(n_shifts)) <= 1)
        # max total minutes
        problem.addConstraint(
            pulp.lpSum(x[day, staff_idx, shift_idx] *
                       instance.shifts[shift_idx].length
                       for day, shift_idx in itertools.product(range(n_days), range(n_shifts))) <= staff.max_total_minutes)

        # min total minutes
        problem.addConstraint(
            pulp.lpSum(x[day, staff_idx, shift_idx] *
                       instance.shifts[shift_idx].length
                       for day, shift_idx in itertools.product(range(n_days), range(n_shifts))) >= staff.min_total_minutes)

        # max shifts
        for shift in instance.shifts:
            shift_idx = shiftids.index(shift.id)
            problem.addConstraint(pulp.lpSum(x[day, staff_idx, shift_idx]
                                             for day in range(n_days)) <= staff.max_shifts[shift.id])

        # max consecutive shifts
        for day in range(n_days):
            # This constraint always assumes that the last day of the previous planning period was a day off and the first day of the next planning period is a day off.
            if day + staff.max_consecutive_shifts >= n_days:
                continue
            problem.addConstraint(
                pulp.lpSum(x[day+offset, staff_idx, shift_idx]
                           for offset, shift_idx in itertools.product(range(staff.max_consecutive_shifts+1), range(n_shifts)))
                <= staff.max_consecutive_shifts)

        # min consecutive shifts
        if staff.min_consecutive_shifts > 1:
            for day in range(n_days):
                # This constraint always assumes that there are an infinite number of consecutive shifts assigned at the end of the previous planning period and at the start of the next planning period.
                if day + staff.min_consecutive_shifts >= n_days:
                    continue
                problem.addConstraint(
                    sum([x[day, staff_idx, shift_idx] for shift_idx in range(n_shifts)])*(staff.min_consecutive_shifts-1) -
                    sum([x[day+1, staff_idx, shift_idx] for shift_idx in range(n_shifts)])*(staff.min_consecutive_shifts-1) +
                    sum([x[day+offset, staff_idx, shift_idx] for offset, shift_idx in
                         itertools.product(range(2, staff.min_consecutive_shifts+1), range(n_shifts))]) >= 0,
                    name=f"min_consecutive_shifts_{day}_{staff.id}")

        # min consecutive days off
        if staff.min_consecutive_days_off > 1:
            for day in range(n_days):
                # This constraint always assumes that there are an infinite number of consecutive days off assigned at the end of the previous planning period and at the start of the next planning period.
                if day + staff.min_consecutive_days_off >= n_days:
                    continue
                problem.addConstraint(
                    sum([x[day, staff_idx, shift_idx] for shift_idx in range(n_shifts)])*(staff.min_consecutive_days_off-1) -
                    sum([x[day+1, staff_idx, shift_idx] for shift_idx in range(n_shifts)])*(staff.min_consecutive_days_off-1) +
                    sum([x[day+offset, staff_idx, shift_idx] for offset, shift_idx in
                         itertools.product(range(2, staff.min_consecutive_days_off+1), range(n_shifts))]) <= staff.min_consecutive_days_off-1,
                    name=f"min_consecutive_days_off_{day}_{staff.id}")

        # max weekends
        for weekend_comb in weekend_combs:
            problem.addConstraint(
                pulp.lpSum(x[day, staff_idx, shift_idx]
                           for day, shift_idx in itertools.product(weekend_comb, range(n_shifts)))
                <= staff.max_weekends)
    for k, v in problem.constraints.items():
        logger.debug(f"{k}:{v}")
    problem.setSolver(pulp.PULP_CBC_CMD(timeLimit=500))
    status = problem.solve()
    logger.info(pulp.LpStatus[status])
    logger.info("objective value = {}".format(pulp.value(problem.objective)))

    ans = np.zeros([n_days, n_staffs, n_shifts])

    for i, j, k in itertools.product(range(n_days), range(n_staffs), range(n_shifts)):
        ans[i, j, k] = pulp.value(x[i, j, k])

    return ans
