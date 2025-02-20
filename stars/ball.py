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
        
        self.position: qtg.QVector2D = qtg.QVector2D(x, y)
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
        
    @property
    def point(self):
        return self.position.toPointF()
    @point.setter
    def point(self, other):
        raise ValueError('Can not set the position')
    
    def __hash__(self):
        return hash((self.point.x(), self.point.y()))
    
    def update(self):
        dx = self.speed * cos(self.angle)
        dy = self.speed * sin(self.angle)
        self.position += qtg.QVector2D(dx, dy)
    
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
        painter.drawEllipse(self.point, self.radius, self.radius)
                
    
    

if __name__ == '__main__':
    ...