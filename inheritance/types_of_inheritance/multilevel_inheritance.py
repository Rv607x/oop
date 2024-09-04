"""
When a class is derived from a class which itself is derived from 
another class, it is called multilevel inheritance.
"""

class Vehicle:      # Parent class
    def setTopSpeed(self, speed):   # defining the set
        self.topSpeed = speed
        print("Top Speed is set to", self.topSpeed)

class Car(Vehicle):     # Child of Vehicle
    def openTrunk(self):
        print("trunk is now open")

class Hybrid(Car):  # child of Car
    def turnOnHybrid(self):
        print("Hybrid is now switched on")

prius = Hybrid()    # creating an object of Hybrid class
prius.setTopSpeed(180)      # Accessing methods from parent class
prius.openTrunk()       # Accessing methods from parent class
prius.turnOnHybrid()    # Accessing methods from child class