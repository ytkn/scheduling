import os
from typing import List, Set, Dict

instance_dir = "instances"


class Shift:
    def __init__(self, id: str, length: int, forbidden: List[str]):
        self.id = id
        self.length = length
        self.forbidden = forbidden


class Staff:
    def __init__(self,
                 id: int,
                 max_shifts: Dict[str, int],
                 max_total_minutes: int,
                 min_total_minutes: int,
                 max_consecutive_shifts: int,
                 min_consecutive_shifts: int,
                 min_consecutive_days_off: int,
                 max_weekends: int):
        self.id = id
        self.max_shifts = max_shifts
        self.max_total_minutes = max_total_minutes
        self.min_total_minutes = min_total_minutes
        self.max_consecutive_shifts = max_consecutive_shifts
        self.min_consecutive_shifts = min_consecutive_shifts
        self.min_consecutive_days_off = min_consecutive_days_off
        self.max_weekends = max_weekends


class DayOff:
    def __init__(self, staff_id: str, day: int):
        self.staff_id = staff_id
        self.day = day


class ShiftRequest:
    def __init__(self, staff_id: str, day: int, shift_id: int, weight: int):
        self.staff_id = staff_id
        self.day = day
        self.shift_id = shift_id
        self.weight = weight


class SectionCover:
    def __init__(self, day: int, shift_id: str, requirement: int, weight_for_under: int, weight_for_over):
        self.day = day
        self.shift_id = shift_id
        self.requirement = requirement
        self.weight_for_under = weight_for_under
        self.weight_for_over = weight_for_over


class Instance:
    def __init__(self,
                 days: int,
                 shifts: List[Shift],
                 staffs: List[Staff],
                 days_off: List[DayOff],
                 on_requests: List[ShiftRequest],
                 off_requests: List[ShiftRequest],
                 section_covers: List[SectionCover]):
        self.days = days
        self.shifts = shifts
        self.staffs = staffs
        self.days_off = days_off
        self.on_requests = on_requests
        self.off_requests = off_requests
        self.section_covers = section_covers


def read_section_horizon(path) -> int:
    is_in_section = False
    ans: int
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_HORIZON":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                ans = int(s_line)
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_shifts(path) -> List[Shift]:
    is_in_section = False
    ans = []
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_SHIFTS":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                l = s_line.split(',')
                ans.append(Shift(l[0], int(l[1]), l[2].split("|")))
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_staffs(path) -> List[Staff]:
    is_in_section = False
    ans = []
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_STAFF":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                l = s_line.split(',')
                max_shifts = {}
                for s in l[1].split('|'):
                    max_shifts[s.split('=')[0]] = int(s.split('=')[1])
                ans.append(Staff(l[0], max_shifts, int(l[2]), int(
                    l[3]), int(l[4]), int(l[5]), int(l[6]), int(l[7])))
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_days_off(path) -> List[DayOff]:
    is_in_section = False
    ans = []
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_DAYS_OFF":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                l = s_line.split(',')
                ans.append(DayOff(l[0], int(l[1])))
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_on_requests(path) -> List[ShiftRequest]:
    is_in_section = False
    ans = []
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_SHIFT_ON_REQUESTS":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                l = s_line.split(',')
                ans.append(ShiftRequest(l[0], int(l[1]), l[2], int(l[3])))
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_off_requests(path) -> List[ShiftRequest]:
    is_in_section = False
    ans = []
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_SHIFT_OFF_REQUESTS":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                l = s_line.split(',')
                ans.append(ShiftRequest(l[0], int(l[1]), l[2], int(l[3])))
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_section_covers(path) -> List[SectionCover]:
    is_in_section = False
    ans = []
    with open(path) as f:
        s_line = f.readline()
        while s_line:
            s_line = s_line.strip('\n')
            if s_line == "SECTION_COVER":
                is_in_section = True
            elif not(len(s_line) == 0 or s_line[0] == '#') and is_in_section:
                l = s_line.split(',')
                ans.append(SectionCover(
                    int(l[0]), l[1], int(l[2]), int(l[3]), int(l[4])))
            elif len(s_line) == 0 and is_in_section:
                break
            s_line = f.readline()
    f.close()
    return ans


def read_instance_from_text(filename) -> Instance:
    path = os.path.join(instance_dir, filename)
    days = read_section_horizon(path)
    shifts = read_shifts(path)
    staffs = read_staffs(path)
    days_off = read_days_off(path)
    on_requests = read_on_requests(path)
    off_requests = read_off_requests(path)
    section_covers = read_section_covers(path)
    return Instance(days, shifts, staffs, days_off, on_requests, off_requests, section_covers)
