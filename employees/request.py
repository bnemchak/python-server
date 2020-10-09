EMPLOYEES = [
    {
        "id": 1,
        "name": "Brock McBroke",
        "location": "77 That place",
        "manager": False,
        "full time": True,
        "hourly rate": 15
    },
    {
        "id": 2,
        "name": "Brook McNotBroke",
        "location": "33 That other place",
        "manager": True,
        "full time": True,
        "hourly rate": 150
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
