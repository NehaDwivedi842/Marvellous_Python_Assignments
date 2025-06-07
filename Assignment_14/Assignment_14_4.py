class Student:
    school_name = "ABC School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name: ",self.name)
        print("Roll No:",self.roll_no)
        print("Name: ",Student.school_name)


s1 = Student("Amit", 101)
s1.display()

Student.school_name = "XYZ School"
s2 = Student("Priya", 102)
s2.display()
