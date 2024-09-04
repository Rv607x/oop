"""
In hierarchical inheritance, more than one class extends, as per the
 requirement of the design, from the same base class. The common 
 attributes of these child classes are implemented inside the base 
 class.

Example:

A Car IS A Vehicle
A Truck IS A Vehicle
"""

class Vehicle:
    def setTopSpeed(self, speed):   # defining the set
        self.topSpeed = speed
        print("Top Speed is set to", self.topSpeed)

class Car(Vehicle):     # child class of vhicle
    pass

class Truck(Vehicle):    # child class of vhicle
    pass

corolla = Car()  # creating an object of the Car class
corolla.setTopSpeed(220)  # accessing methods from the parent class

volvo = Truck()  # creating an object of the Truck class
volvo.setTopSpeed(180)  # accessing methods from the parent class
