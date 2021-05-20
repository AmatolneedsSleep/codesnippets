"""
Created on Mon Jan 27 19:03:45 2020

@author: wang_
"""
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640,480)) #double brackets, be aware
pygame.display.update()

"Basic Colours"

#Red and Browns
red = (255,0,0)
fireBrick = (178,34,34)
brown = (98,74,46)

#Pinks and Purples
pink = (255,200,200)
purple = (135,0,135)

#Yellows and oranges
yellow = (255,255,0)
orange = (255,179,0)

#Greens
green = (0, 255, 0)
mint = (152,251,152)
darkGreen = (0,100,0)
lawnGreen = (127,255,0)

#Blues
teal = (0,135,135)
blue = (0, 0, 255)
darkBlue = (0,0,128)
skyBlue = (153,255,255)
veryLightBlue = (204,255,255)

#Blacks
white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)


def drawHouse(x,y, width, height , screen, color):
    points = [(x , y - ((2/3.0)* height)),
              (x, y) ,
              (x + width,y),
              (x + width, y - ((2/3.0)* height)),
              (x , y - ((2/3.0)* height)),
              (x + width/2.0, y - height), 
              (x + width, y - ((2/3.0)* height))]
    lineThick = 6 
    pygame.draw.lines(screen, black , False, points, lineThick)
    
def drawHouseA(x,y, width, height , screen, color):
    points = [(x , y - ((2/3.0)* height)),
              (x, y) ,
              (x + width,y),
              (x + width, y - ((2/3.0)* height)),
              (x , y - ((2/3.0)* height)),
              (x + width/2.0, y - height), 
              (x + width, y - ((2/3.0)* height))]
    lineThick = 7
    pygame.draw.lines(screen, yellow, False, points, lineThick)
    
def drawHouseB(x,y, width, height , screen, color):
    points = [(x , y - ((2/3.0)* height)),
              (x, y) ,
              (x + width,y),
              (x + width, y - ((2/3.0)* height)),
              (x , y - ((2/3.0)* height)),
              (x + width/2.0, y - height), 
              (x + width, y - ((2/3.0)* height))]
    lineThick = 6 
    pygame.draw.lines(screen, black , False, points, lineThick)
    

    
  


    



screen.fill(veryLightBlue) #Background sky
pygame.draw.rect(screen, green, [0,240,640,480]) #Foreground
pygame.draw.rect(screen, green, [0,200, 240,640]) #the one hill
drawHouse(260,240,30,30, screen, black) # houses
drawHouseA(295,240,30,60, screen, yellow)
drawHouseB(330,240,60,30, screen, black)
pygame.draw.rect(screen, brown, [50,80,10,120]) #Tree Trunk
pygame.draw.circle(screen, darkGreen, [50, 100], 30) #Tree Leaves

pygame.display.update() #This is very IMPORTANT, Take note

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #This is the X button in the corner, very important. 
            pygame.quit()
            sys.exit()
    pygame.display.update()
    












































