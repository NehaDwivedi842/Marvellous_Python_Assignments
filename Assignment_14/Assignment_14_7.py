class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()
        print("Subject",self.subject)
        print("Salary:", self.salary)


t = Teacher("Raj", 40, "Math", 50000)
t.display()
