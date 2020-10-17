import sqlite3
import json

from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Brock McBroke",
        "employee": "77 That place",
        "manager": False,
        "full time": True,
        "hourly rate": 15
    },
    {
        "id": 2,
        "name": "Brook McNotBroke",
        "employee": "33 That other place",
        "manager": True,
        "full time": True,
        "hourly rate": 150
    }
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.employee,
            a.manager,
            a.full_time,
            a.hourly_rate,
        FROM employee a
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['employee'], row['manager'], row['full_time'], row['hourly_rate'])

            employees.append(employee.__dict__)

    return json.dumps(employees)

def get_single_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.employee,
            a.manager,
            a.full_time,
            a.hourly_rate,
        FROM employee a
        WHERE a.id = ?
        """, ( id ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['employee'], data['manager'], data['full_time'], data['hourly_rate'])

        return json.dumps(employee.__dict__)

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1

    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
