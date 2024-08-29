"""
Problem statement:
Implement the complete Student class by completing the tasks below

Task
Implement the following properties as private:

- name
- rollNumber

Include the following methods to get and set the private properties above:

- getName()
- setName()
- getRollNumber()
- setRollNumber()

Implement this class according to the rules of encapsulation.

Input
Checking all the properties and methods

Output
Expecting perfectly defined fields and getter/setters

"""

class Student:
    def __init__(self, name = None, roleNumber = None):
        self.__name = name
        self.__roleNumber = roleNumber

    def setName(self, x):
        self.__name = x

    def getName(self):
        return (self.__name)

    def setRollNumber(self, y):
        self.__roleNumber = y

    def getRollNumber(self):
        return(self.__roleNumber)

Steve = Student("stevo", 12345)
print("Name before setting name ", Steve.getName())
Steve.setName("vosti")
print("Name after setting new name is ", Steve.getName())
print(Steve.getRollNumber())