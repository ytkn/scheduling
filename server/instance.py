from typing import List, Set, Dict


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
