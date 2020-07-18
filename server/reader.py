import xmljson
import os
import json
from lxml.etree import parse
from typing import List, Set, Dict

solution_dir =  "instances_solutions/Solutions/XML"
instance_dir = "instances"

class OnRequest:
  def __init__(self, shift_id:str, day:int, weight:int):
    self.shift_id = shift_id
    self.day = dey
    self.weight = weight

class OffRequest:
  def __init__(self, day:int, weight:int):
    self.day = day
    self.weight = weight

class ShiftAssign:
  def __init__(self, day:int, shift_id:str):
    self.day = day
    self.shift_id = shift_id

class Instance:
  shift_covers: Set[ShiftCover]
  employees: List[Employee]
  def __init__(self, employees:List[Employee]):
    self.shift_covers = set()
    self.employees = employees

  def score(self) -> int:
    return self._employee_violences() + self._shift_cover_violences()

  def _shift_cover_violences(self) -> int:
    return sum([_shift_cover_violence(shift_cover) for shift_cover in self.shift_covers])

  def _shift_cover_violence(self, shift_cover:ShiftCover) -> int:
    cover = sum([(1 if shift_cover.day in employee.shift_assings else 0) for employee in self.employees])
    return (cover-shift_cover.requirement)*shift_cover.weight_for_over if cover > shift_cover.requirement else (shift_cover.requirement-cover)*shift_cover.weight_for_under

  def _employee_violences(self) -> int:
    return sum([employee.on_request_violences()+employee.off_request_violences() for employee in self.employees])

class ShiftCover:
  def __init__(self, day:int, shift_id:str, requirement:int, weight_for_under: int, weight_for_over):
    self.day = day
    self.shift_id = shift_id
    self.requirement = requirement
    self.weight_for_under = weight_for_under
    self.weight_for_over = weight_for_over

class Employee:
  off_requests : Dict[int, OffRequest]
  on_requests : Dict[int, OnRequest]
  fixed_off_days : Set[int]
  shift_assings : Set[ShiftAssign]
  max_shifts: Dict[str, int]
  def __init__(self, 
               id:int,
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
    self.off_requests = {} 
    self.on_requests = {}
    self.fixed_off_days = set()
    self.shift_assings = set() 

  def off_request_violences(self) -> int:
      return sum([self._off_request_violence(assign) for assign in self.shift_assings])

  def _off_request_violence(self, assign:ShiftAssign) -> int:
      return self.off_requests[assign.day].weight if assign.day in self.off_requests  else 0

  def on_request_violences(self) -> int:
      return sum([self._on_request_violence(request) for request in self.on_requests])

  def _on_request_violence(self, request:OnRequest) -> int:
      return request.weight if ShiftAssign(request.day, request.shift_id) in self.shift_assings else 0 

def read_solution(file):
    tree = parse(os.path.join(solution_dir, file))
    root = tree.getroot()
    d = xmljson.yahoo.data(root)
    return d["Roster"]["Employee"]

def read_instance(file):
    tree = parse(os.path.join(instance_dir, file))
    root = tree.getroot()
    d = xmljson.yahoo.data(root)
    return d
        
if __name__ == "__main__":
    sol = read_solution("Instance1.Solution.607.roster")
    with open('solution.json', 'w') as fw:
        json.dump(sol, fw, indent=2)
    instance = read_instance("Instance1.ros")

