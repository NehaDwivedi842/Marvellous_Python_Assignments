class Employee:
    def __init__(self, name, department, salary):
        self.name = name               # Public
        self._department = department  # Protected
        self.__salary = salary         # Private

    def display(self):
        print("Name:")
        print(self.name)

        print("Department:")
        print(self._department)

        print("Salary:")
        print(self.__salary)


e = Employee("Aarav", "IT", 70000)
e.display()
print(e.name)
print(e._department)
