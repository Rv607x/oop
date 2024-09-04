class Vehicle:
    def __init__(self, make:str, color:str, model:str):
        self.make = make
        self.color = color
        self. model = model
    
    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)
    
class Car(Vehicle):
    def __init__(self, make, color, model, doors: int):
        super().__init__(make, color, model)
        self.doors = doors
        
    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)
        
obj1 = Car("Bj40", "Blue", "2022", 2)
obj1.printCarDetails()