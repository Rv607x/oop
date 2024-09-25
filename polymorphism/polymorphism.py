"""
a Shape class, which is the base class while many shapes like Rectangle 
and Circle extending from the base class are derived classes. These 
derived classes inherit the getArea() method and provide a shape-specific 
implementation, which calculates its area.
"""

class Shape:
    def __init__(self, sides = 0):
        self.sides = sides

    def get_area(self):
        pass

"""
The Rectangle class is extended from the Shape class. It inherits 
the sides property from the Shape class and defines new properties, 
width and height. The method getArea() returns the area of the rectangle.
"""
class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        self.lenght = length
        self.width = width
        self.sides = 4
    
    def get_area(self):
        return (self.lenght * self.width)
    
class Circle(Shape):
    def __init__(self, radius = 0):
        self.radius = radius
    
    def get_area(self):
        return (self.radius * self.radius * 3.14)
    
shapes = [Rectangle(6, 10), Circle(7)]
print("Area or rectangle is:", shapes[0].get_area())
print("Area of circle is:", shapes[1].get_area())