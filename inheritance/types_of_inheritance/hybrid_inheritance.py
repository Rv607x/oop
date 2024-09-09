"""
A type of inheritance which is a combination of Multiple and Multi-level inheritance is called hybrid inheritance.

CombustionEngine IS A Engine.
ElectricEngine IS A Engine.
HybridEngine IS A ElectricEngine and a CombustionEngine.
"""

class Engine:       # Parent class
    def set_power(self, power):
        self.power = power

class CombustionEngine(Engine):      # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine(Engine):        # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Engine Power is", self.power)
        print("Tank Capacity is", self.tankCapacity)
        print("charge capacity:", self.chargeCapacity)

car = HybridEngine()
car.set_power("3000 cc")
car.setTankCapacity("100 litres")
car.setChargeCapacity("250 W")
car.printDetails()