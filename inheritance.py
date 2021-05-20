# -*- coding: utf-8 -*-
"""
Created on Tues Oct 27 18:59:08 2020

@author: wang

"""

#inheritance practice
class Vehicle:
    def __init__(self, model="", make="", colour=""):
        self.carNoise = "Vroom"
        self.model = model
        self.make = make
        self.colour = colour
        self.wheels = 0
        self.__License = ""
   
    def showInfo(self):
        print("~~~", self.model, "~", self.make, "~", self.colour, "~~~")
        if self.wheels > 0:
            print("Wheel Count:", self.wheels)
        if self.__License != "":
            print("License Plate:", self.__getLicense())
        if self.doors > 0: 
            print("Door Count:", self.doors)
            
    """
    Getters and Setters still confused on these but eh

    """
    def setLicense(self, plateNum):
        self.__License = plateNum
    
    def __getLicense(self):
        return self.__License
    
    #Getters and Setters with Public variables
    def setWheels(self, wheels):
        self.wheels = wheels
        
    def getWheels(self):
        return self.wheels
    
    def __str__(self):
        return self.carNoise
    
#child Class
class Sedan(Vehicle):
    def __init__(self, model, make, colour):
        super().__init__(model, make, colour)
        self.carNoise  = "Veeeeeerooooom!"
        self.doors = 4
             
class Motorcycle(Vehicle):
    def __init__(self, model, make, colour):
        super().__init__(model, make, colour)
        self.carNoise = "that terrible noise you hear on the highway that gives you a heart attack!"
        self.doors = 0

myVehicle = Vehicle()
mySedan = Sedan("Honda", "Civic", "Sliver")
print(myVehicle)
print(mySedan)
mySedan.showInfo()

myMCycle = Motorcycle("Generic Motorcycle", "Bike", "Blue")
print(myMCycle)
myMCycle.setWheels(2)
myMCycle.setLicense("123 ABC")
myMCycle.showInfo()