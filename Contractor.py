from Employee import Employee
from typing import override

class Contractor(Employee):
    @override
    def __init__(self, id, name, address, birth_year, number_of_projects, project_rate):
        super().__init__(id, name, address, birth_year)
        self.number_of_projects: int = number_of_projects
        self.project_rate: int = project_rate

    @override
    def calculateSalary(self):
        return  self.number_of_projects * self.project_rate


    def __str__(self):
        return super().__str__() + (f", Projects: {self.number_of_projects}, Project Rate: {self.project_rate}, "
                                    f"Salary: {self.calculateSalary()}")



