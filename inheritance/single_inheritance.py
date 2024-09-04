"""
In single inheritance, there is only a single class extending from another class
"""

class Vehicle:  # Parent class
    def setTopSpeed(self, speed):   # define the set
        self.topSpeed = speed
        print("Top Speed is set to", self.topSpeed)

class Car(Vehicle):
    def openTrunk(self):
        print("trunk is now open")

corrolla = Car()
corrolla.setTopSpeed(20)
corrolla.openTrunk()