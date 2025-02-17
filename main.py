from worker import Worker
from manager import Manager
from contractor import Contractor

def main():
    worker = Worker(1, "Alice", "123 Main St", 1990, 8, 20)
    manager = Manager(2, "Bob", "456 Park Ave", 1985, 10, 500)
    contractor = Contractor(3, "Charlie", "789 Elm St", 1992, 5, 2000)

    return worker, manager, contractor

if __name__ == "__main__":
    worker, manager, contractor = main()
    print(worker)
    print(manager)
    print(contractor)