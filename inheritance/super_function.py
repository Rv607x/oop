"""
The use of super() comes into play when we implement inheritance. 
It is used in a child class to refer to the parent class without 
explicitly naming it. It makes the code more manageable, and there
 is no need to know the name of the parent class to access its 
 attributes.
"""

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