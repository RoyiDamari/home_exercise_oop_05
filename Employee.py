from abc import ABC, abstractmethod
from datetime import datetime


class Employee(ABC):
    @abstractmethod
    def __init__(self, id: int, name: str, address: str, birth_year: int):
        self.id = id
        self.name = name
        self.address = address
        self.birth_year = birth_year
        self.age: int = self.get_age()

    def get_age(self):
        return datetime.now().year - self.birth_year

    @abstractmethod
    def calculateSalary(self):
        pass

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}, Age: {self.age}"



