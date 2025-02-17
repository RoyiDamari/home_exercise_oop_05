from employee import Employee
from typing import override

class Worker(Employee):
    @override
    def __init__(self, id, name, address, birth_year, hours_per_day, hour_rate):
        super().__init__(id, name, address, birth_year)
        self.hours_per_day: int = hours_per_day
        self.hour_rate: int = hour_rate

    @override
    def calculateSalary(self):
        return self.hours_per_day * self.hour_rate


    def __str__(self):
        return super().__str__() + (f", Hours/Day: {self.hours_per_day}, Hour Rate: {self.hour_rate},"
                                    f" Salary: {self.calculateSalary()}")
