class Employee():
    def __init__(self, id, name, employee, manager, full_time, hourly_rate):
        self.id = id
        self.name = name
        self.employee = employee
        self.mangager = manager
        self.full_time = full_time
        self.hourly_rate = hourly_rate

    def __repr__(self):
        return f"{self.name} from {self.employee}"

employee = Employee(1, 'Brock McBroke', '77 That place', False, True, 15)
