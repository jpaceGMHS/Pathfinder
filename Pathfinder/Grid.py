import pygame as py
import random

class Cell:
    def __init__(self):
        pass
    
    
class Grid:
    def __init__(self, Screen:py.display, Dimension:int):
        self.Screen = Screen
        self.Dimension = Dimension
        self.Cells = [[]]
        self.Line_Weight = 1
        self.Cell_size = int(Screen.get_width() / Dimension) - self.Line_Weight
        
    def _build_Grid(self):
        pass
    
    # Returns the cell based on location in the 2D List
    def Get_Cell_byPosition(self, location):
        pass
    
    # Returns the Cell based on location on screen
    def Get_Cell_byScreenLocation(self, location):
        pass
    
    
    def Draw(self):
        for ii in range(0, self.Dimension):
            for jj in range(0, self.Dimension):
                py.draw.rect(self.Screen, 
                             (random.randint(0, 255),255,255), 
                             py.Rect(jj*(self.Cell_size + self.Line_Weight),
                                     ii*(self.Cell_size + self.Line_Weight),
                                     self.Cell_size,self.Cell_size))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        