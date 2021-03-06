import pygame
import numpy as np

from . object import Object

"""
The class describes rope segment
right side attached to previous
left side attached to next
"""
class Segment(Object):
    g = 9.8
    F = 0 #perpendicular force

    def __init__(self, x, y, l, d, angle, m, speed=(0, 0), w = 0):
        self.m = m                          #the mass 
        self.i = m * (l**2 / 3 + d**2 / 8)  #the impulse #recalculate the impulse
        self.l = l                          #the length
        self.d = d                          #the diameter
        
        self.x = x                          #the x coordinate
        self.y = y                          #the y coordinate
        self.angle = angle                  #angle between vertical and the line of symmetry (clockwise)
        self.speed = speed                  #the speed (on x and y coordinate)
        self.w = w                          #the rotation speed (clockwise)
    
    
    @property
    def top_left(self): #top_left
        return (self.x + self.l/2 * np.sin(self.angle) - self.d/2 * np.cos(self.angle), self.y - self.l/2 * np.cos(self.angle) - self.d/2 * np.sin(self.angle))
    
    @property
    def bot_left(self): #bot_left
        return (self.x - self.l/2 * np.sin(self.angle) - self.d/2 * np.cos(self.angle), self.y + self.l/2 * np.cos(self.angle) - self.d/2 * np.sin(self.angle))

    @property
    def top_right(self): #top_right
        return (self.x + self.l/2 * np.sin(self.angle) + self.d/2 * np.cos(self.angle), self.y - self.l/2 * np.cos(self.angle) + self.d/2 * np.sin(self.angle))
    
    @property
    def bot_right(self): #bot_right
        return (self.x - self.l/2 * np.sin(self.angle) + self.d/2 * np.cos(self.angle), self.y + self.l/2 * np.cos(self.angle) + self.d/2 * np.sin(self.angle))

    @property
    def top_mid(self): #top_mid
        return (self.x + self.l/2 * np.sin(self.angle), self.y - self.l/2 * np.cos(self.angle))

    @property
    def bot_mid(self): #bot_mid
        return (self.x - self.l/2 * np.sin(self.angle), self.y + self.l/2 * np.cos(self.angle))

    def set_top_mid(self, x, y): #top_mid
        self.x = x - self.l/2 * np.sin(self.angle)
        self.y = y + self.l/2 * np.cos(self.angle)

    def set_bot_mid(self, x, y): #bot_mid
        self.x = x + self.l/2 * np.sin(self.angle)
        self.y = y - self.l/2 * np.cos(self.angle)