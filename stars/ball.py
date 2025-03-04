from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from math import sin, cos, radians, pi
from random import randint



class Ball:
    def __init__(
        self, 
        x: int, y: int, 
        speed: int = 0, angle: int | float= 0, 
        color: qtg.QColor = qtg.QColor(255, 0, 0, 180), radius: int = 15
        ):
        
        self.position: qtg.QVector2D = qtg.QVector2D(x, y)
        self.color = color
        
        self.radius = radius
        self._MAX_SIZE = radius + radius * 0.3
        self._MIN_SIZE = radius - radius * 0.9
        self.radius_change_size = randint(1, 4) / 12
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
    
    def _inflate(self):
        self.radius += self.radius_change_size
        if self.radius > self._MAX_SIZE:
            self.radius = 20
            self.radius_change_size = -self.radius_change_size
        elif self.radius < self._MIN_SIZE:
            self.radius = 10
            self.radius_change_size = -self.radius_change_size
    
    def draw(self, painter: qtg.QPainter):
        gradient = qtg.QRadialGradient(self.point, self.radius)
        gradient.setColorAt(0, self.color)
        gradient.setColorAt(0.5, self.color.lighter(120))
        gradient.setColorAt(1, qtg.QColor(0, 0, 0, 0))
        
        self._inflate()

        painter.setBrush(qtg.QBrush(gradient))
        painter.setPen(qtg.Qt.NoPen)
        painter.drawEllipse(self.point, self.radius, self.radius)
        
                
    
    

if __name__ == '__main__':
    ...