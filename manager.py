from employee import Employee
from typing import override

class Manager(Employee):
    @override
    def __init__(self, id, name, address, birth_year, number_of_employees, employee_rate):
        super().__init__(id, name, address, birth_year)
        self.number_of_employees: int = number_of_employees
        self.employee_rate: int = employee_rate

    @override
    def calculateSalary(self):
        return self.number_of_employees * self.employee_rate


    def __str__(self):
        return super().__str__() + (f", Employees Managed: {self.number_of_employees}, "
                                    f"Employee Rate: {self.employee_rate}, Salary: {self.calculateSalary()}")
