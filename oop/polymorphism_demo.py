# This script will inherit methods from parent class and implement polymorphism
import math

# define base class
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError

# define classes derived from base class
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self): # child class implementing its own behaviour
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2