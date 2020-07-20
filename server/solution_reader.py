import xmljson
import os
import json
import numpy as np
from lxml.etree import parse
from instance import Instance
from instance_reader import read_instance_from_text
from typing import List, Set, Dict

solution_dir = "instances_solutions/Solutions/XML"


def read_solution_from_xml(file: str, instance: Instance):
    shiftids = [shift.id for shift in instance.shifts]
    staffids = [staff.id for staff in instance.staffs]
    n_days = instance.days
    n_staffs = len(instance.staffs)
    n_shifts = len(instance.shifts)

    tree = parse(os.path.join(solution_dir, file))
    root = tree.getroot()
    d = xmljson.yahoo.data(root)
    employees = d['Roster']['Employee']

    x = np.zeros([n_days, n_staffs, n_shifts])

    for employee in employees:
        staff_idx = staffids.index(employee['ID'])
        for assign in employee['Assign']:
            day = int(assign['Day'])
            shift_idx = shiftids.index(assign['Shift'])
            x[day][staff_idx][shift_idx] = 1
    return x


def list_solutions(instanceName: str) -> List[str]:
    return list(filter(lambda x: f"{instanceName}." in x,  os.listdir(solution_dir)))
