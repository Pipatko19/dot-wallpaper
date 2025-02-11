import random
from typing import Optional
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from typing import NamedTuple
from math import sin, cos, radians, pi


class Position:
    
    def __init__(self, x, y, speed=1, angle=0):
        self.position = qtc.QPointF(x, y)
        self.speed = speed
        self._angle = radians(angle) #in degrees
    
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, val):
        #self._angle = val % (2 * pi)
        self._angle = val
    
    def update(self):
        dx = self.speed * cos(self.angle)
        dy = self.speed * sin(self.angle)
        
        self.position += qtc.QPointF(dx, dy)
    
    def reflect(self, axis=None):
        """Reflects the angle. If axis=None, reflect both axis, if axis=0 reflect x, else reflect y"""
        match axis:
            case 0:
                self.angle = -self.angle
            case 1:
                self.angle = pi - self.angle
            case _:
                ...



class Ball(Position):
    def __init__(
        self, 
        x: int, y: int, 
        speed: int =1, angle: int | float= 0, 
        color: qtg.QColor = qtg.QColor(255, 0, 0, 180), radious: int = 10
        ):
        super().__init__(x, y, speed, angle)
        self.color = color
        self.radious = radious

    

if __name__ == '__main__':
    ...