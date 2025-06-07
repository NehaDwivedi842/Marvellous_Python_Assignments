class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")
        print("Engine check complete")

v = Vehicle()
v.start()

c = Car()
c.start()
