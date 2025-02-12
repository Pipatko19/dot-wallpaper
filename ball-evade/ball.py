from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from math import sin, cos, radians, pi

class Ball:
    def __init__(
        self, 
        x: int, y: int, 
        speed: int = 0, angle: int | float= 0, 
        color: qtg.QColor = qtg.QColor(255, 0, 0, 180), radius: int = 10
        ):
        
        self.position = qtc.QPointF(x, y)
        self.color = color
        self.radius = radius
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
                self.angle = self.angle + pi
    
    def draw(self, painter: qtg.QPainter):
        painter.setBrush(qtg.QBrush(self.color))
        painter.drawEllipse(self.position, self.radius, self.radius)
                
class Atractor(Ball):
    def __init__(self, radius = 5, color: qtg.QColor = qtg.QColor(255, 255, 255, 180)):
        super().__init__(x=0, y=0, radius=radius, color=color)
    
    def update(self, position: qtc.QPointF = None):
        'Should be stationary or be on top of the cursor'
        ...
        if position is None:
            return
        self.position = position
    
    

if __name__ == '__main__':
    ...