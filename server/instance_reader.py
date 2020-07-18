import os
from typing import List, Set, Dict
from instance import Instance, Shift, Staff, SectionCover, ShiftRequest, DayOff

instance_dir = "instances"


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
