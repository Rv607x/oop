"""
In inheritance, in order to create a new class based on an existing class, we use the following terminology:

Parent Class (Super Class or Base Class): This class allows the reuse of its public properties in another class.
Child Class (Sub Class or Derived Class): This class inherits or extends the superclass.

"""

# Create a parent class called vehicle
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print("Manufacture:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)
        
# Now create a child class called car from vehicle
class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors
        
    def printCarDetails(self):
        self.printDetails
        print("Doors:", self.doors)
        
        
obj1 = Car("BJ40", "Cream", "2021", 2)
obj1.printCarDetails()
