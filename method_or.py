from math import pi

class Shape:
    def __init__(self,name):#Constructor
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am a two dimensional shape"   
    def __str__(self):
        return self.name
    
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")    
        self.length = length
        
    def area(self):
        return self.length**2
    
    def fact(self):
        return "Squares have each an angle equal to 90 degress"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
        
    def area(self):
        return pi*self.radius**2    
    
rombus = Square(4)   
circle = Circle(7) 
print(rombus)
print(rombus.area())
print(rombus.fact())
print()
print(circle)
print(circle.area())
print(circle.fact())
        
        
        
    