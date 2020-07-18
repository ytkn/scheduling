import numpy as np
import pulp
import itertools
import instance_reader
from instance_reader import Instance


def init(instance: Instance):
    weekends = [[5, 6], [12, 13]]
    weekend_combs = [[5, 12], [5, 13], [6, 12], [6, 13]]
    shiftids = [shift.id for shift in instance.shifts]
    staffids = [staff.id for staff in instance.staffs]
    n_days = instance.days
    n_staffs = len(instance.staffs)
    n_shifts = len(instance.shifts)
    problem = pulp.LpProblem(name="scheduling", sense=pulp.LpMinimize)
    x = {(i, j, k): pulp.LpVariable(name='x_{}_{}_{}'.format(i, j, k), cat="Binary")
         for i, j, k in itertools.product(range(n_days), range(n_staffs), range(n_shifts))}

    t = {i: pulp.LpVariable(name='t_{}'.format(i), cat=pulp.LpInteger)
         for i in range(len(instance.section_covers))}

    # section cover
    for i in range(len(instance.section_covers)):
        section_cover = instance.section_covers[i]
        problem.objective += t[i]
        day = section_cover.day
        shift_idx = shiftids.index(section_cover.shift_id)
        problem.addConstraint(
            section_cover.weight_for_under*(section_cover.requirement -
                                            pulp.lpSum(x[day, staff_idx, shift_idx] for staff_idx in range(n_staffs))) <= t[i])

        problem.addConstraint(
            section_cover.weight_for_over*(pulp.lpSum(x[day, staff_idx, shift_idx] for staff_idx in range(n_staffs))
                                           - section_cover.requirement) <= t[i])

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
        staff_id = staffids.index(day_off.staff_id)
        day = day_off.day
        for shift_idx in range(n_shifts):
            problem.addConstraint(x[day, staff_id, shift_idx] >= 0)
            problem.addConstraint(x[day, staff_id, shift_idx] <= 0)

    # TODO one shift for a day
    # section_staff
    for staff in instance.staffs:
        staff_idx = staffids.index(staff.id)
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
        for day in range(n_days):
            # This constraint always assumes that there are an infinite number of consecutive shifts assigned at the end of the previous planning period and at the start of the next planning period.
            if day + staff.min_consecutive_shifts >= n_days:
                continue
            problem.addConstraint(
                pulp.lpSum(x[day+offset, staff_idx, shift_idx] if offset > 0 and offset < staff.min_consecutive_shifts else 1-x[day+offset, staff_idx, shift_idx]
                           for offset, shift_idx in itertools.product(range(staff.min_consecutive_shifts+1), range(n_shifts)))
                <= staff.min_consecutive_shifts)

        # min consecutive days off
        for day in range(n_days):
            # . This constraint always assumes that there are an infinite number of consecutive days off assigned at the end of the previous planning period and at the start of the next planning period.
            if day + staff.min_consecutive_days_off >= n_days:
                continue
            problem.addConstraint(
                pulp.lpSum(1-x[day+offset, staff_idx, shift_idx] if offset > 0 and offset < staff.min_consecutive_days_off else x[day+offset, staff_idx, shift_idx]
                           for offset, shift_idx in itertools.product(range(staff.min_consecutive_days_off+1), range(n_shifts)))
                <= staff.min_consecutive_days_off)

        # max weekends
        n_weekends = len(weekends)
        for weekend_comb in weekend_combs:
            problem.addConstraint(
                pulp.lpSum(x[day, staff_idx, shift_idx]
                           for day, shift_idx in itertools.product(weekend_comb, range(n_shifts)))
                <= staff.max_weekends)

    print(problem.constraints)
    status = problem.solve()
    print(pulp.LpStatus[status])
    print("objective value = {}".format(pulp.value(problem.objective)))

    for i in range(n_days):
        print(f"day:{i}", end=" ")
        for j, k in itertools.product(range(n_staffs), range(n_shifts)):
            print("{}:{}".format(j, pulp.value(x[i, j, k])), end=" ")
        print(pulp.value(t[i]))


def main():
    instance = instance_reader.read_instance_from_text("Instance1.txt")
    init(instance)


if __name__ == "__main__":
    main()
