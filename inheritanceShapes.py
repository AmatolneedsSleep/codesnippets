# -*- coding: utf-8 -*-
"""
Created on Tue Nov 3 9:03:53 2020

@author: wang_
"""

import math

#Parent
class Shape:
    def __init__(self, shapeType, colour):
        self.shapeType = shapeType
        self.colour = colour
        self.perim = 0
        self.area = 0
        #Overloading
        self.length = 0
        self.width = 0
        self.radius = 0
    
    #"Error" messages 
    def getArea(self):
        print(self.shapeType,"Area Not Coded!!")
 
    def getPerimeter(self):
        print(self.shapeType,"Perimeter Not Coded!!")
        
        
    def showLength(self):
        if self.length == 0:
            print(self.shapeType, "does not have a length!")
        else:
            print("Length:", self.length)
        
    def showWidth(self):
        if self.width == 0:
            print(self.shapeType, "does not have a width!")
        else:
            print("Width:", self.width)
        
    def showRadius(self):
        if self.radius == 0:
            print(self.shapeType, "does not have a radius!")
        else:
            print("Radius:", self.radius)
        
        
    def __str__(self):
        self.getArea()
        self.getPerimeter()
        output = ""
        output += "~~~" + self.colour + "~" + self.shapeType + "~~~\n"
        output += "Perimeter: " + str(self.perim) + "\n"
        output += "Area: " + str(self.area) + "\n"
        output += "~~~~~~~~~~~~~~~~~~~~~~~~~"
        return output
        
#Children
class Rectangle(Shape):
    def __init__(self, length, width, colour):
        super().__init__("Rectangle", colour)
        self.length = length
        self.width = width
        
    def getArea(self):
        self.area = self.length * self.width
    
    def getPerimeter(self):
        self.perim = 2 * (self.length + self.width)
        
        
class Square(Shape):
    def __init__(self, length, colour):
        super().__init__("Square", colour)
        self.length = length
        
    def getArea(self):
        self.area = self.length**2
    
    def getPerimeter(self):
        self.perim = 4 * self.length
        
class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__("Circle", colour)
        self.radius = radius
        
    def getArea(self):
       self.area = math.pi * (self.radius**2)
    
    def getPerimeter(self):
        self.perim = 2 * math.pi * self.radius
        
    #declaring
mySquare = Square(10, "Orange")
myRect = Rectangle(3, 9, "Blue")
myCircle = Circle(8, "Green")
print(mySquare)
print(myCircle) 

#making sure everythings working probably lol
myRect.showLength()
myRect.showRadius()
myCircle.showLength()