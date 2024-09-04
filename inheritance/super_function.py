"""
The use of super() comes into play when we implement inheritance. 
It is used in a child class to refer to the parent class without 
explicitly naming it. It makes the code more manageable, and there
 is no need to know the name of the parent class to access its 
 attributes.
"""

print("****** Accessing parent class properties using Super() Function **********")
print("")
class Vehicle:      # parent class
    fuelCap = 90
    
class Car(Vehicle):
    fuelCap = 50
    
    def display(self):
        # Accessing fuelcap from Vehicle class using super()
        print("Fuel cap from the vehicle class:", super().fuelCap)
        
        # Accessing fuelCap from the Car class using self
        print("Fuel cap from the Car class:", self.fuelCap)
        
obj1 = Car()
obj1.display()

print("")
print("****************** Calling the parent class methods *******************")
print("")
"""
Just like properties, super() is also used with methods. Whenever a 
parent class and the immediate child class have any methods with the
 same name, we use super() to access the methods from the parent 
 class
"""

class Vehicle2:     # defining the parent class
    def display(self):      # defining display method in parent class
        print("I am from the Vehicle class")
        
class Car2(Vehicle2):   # defining child class
    # defining method in child class
    def display(self):
        super().display()
        print("I am from Car class")

obj2 = Car2()
obj2.display()