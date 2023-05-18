# imports libraries
import random
import os
import pygame
import sys
import math
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw() #to hide the main Tkinter window

N = 6
EMPTY_SPACE = '_'
ICE_CREAM_TRUCK = 'A'
START_ROW = 2

class Rectangle: #rectangle class

    def __init__(self, orientation, size, row, column, target=False):
        perSq = 120 #one square is 120x120
        self.startX = column * perSq #starting x-coordinate
        self.startY = row * perSq #starting y-coordinate
        self.orientation = orientation
        self.size = size
        
        if self.orientation == "h": #for horizontal cars
            length = perSq * size
            self.extendX = length #How much the x-coordinate extends by
            self.extendY = perSq #How much the y-coordinate extends by
            self.colour = (237, 149, 108) #Brown-ish Orange
            self.startLimitX = 0 #Starting x coordinate of where the car can be positioned
            self.startLimitY = self.startY #Starting y coordinate of where the car can be positioned
            self.endLimitX = 6 * perSq - length + perSq #Ending x coordinate of where the car can be positioned
            self.endLimitY = self.startY + self.extendY #Ending x coordinate of where the car can be positioned
            
        else: #same as above, but for vertical, so swap x and y
            length = perSq * size
            self.extendX = perSq
            self.extendY = length
            self.colour = (237, 149, 108)
            self.startLimitX = self.startX
            self.startLimitY = 0
            self.endLimitX = self.startX + self.extendX
            self.endLimitY = 6 * perSq - length + perSq

        if target: #if it is the first car (car needed to get across)
            self.colour = (204, 0, 0) #make it its own different colour to differentiate

        self.currentX = self.startX + 0 #current x-coordinate of car
        self.currentY = self.startY + 0 #current y-coordinate of car

        self.rectDrag = False #boolean if the car is currently being dragged or not
        self.rect = pygame.Rect(self.startX, self.startY, self.extendX, self.extendY) #make rectangle object


