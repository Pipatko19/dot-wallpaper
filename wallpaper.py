import sys
import random
from collections import namedtuple
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc

from ball import Ball

BALL_RADIOUS = 15
OFFSET = BALL_RADIOUS + 10
BALL_COUNT = 200
BALL_SPEED = 5

class Wallpaper(qtw.QWidget):
    key_pressed = qtc.Signal(str)
    def __init__(self, geometry: qtc.QRect):
        """Wallpaper constructor"""
        super().__init__()
        self.setGeometry(geometry)
        #Main UI code goes here

        self.balls = [
            Ball(
                x=random.randint(OFFSET, self.width() - OFFSET),
                y=random.randint(OFFSET, self.height() - OFFSET),
                speed=random.choice([-BALL_SPEED, BALL_SPEED]),
                angle=random.randint(0, 359),
                color=qtg.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 180),
                radious = BALL_RADIOUS
            )
            for _ in range(BALL_COUNT)
            ]
        
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.update_positions)
        self.timer.start(30)
        
        self.key_pressed.connect(self.spin)
        #End main UI code
        self.show()
    
    def update_positions(self):
        for ball in self.balls:
            ball.update()
            x, y = ball.position.x(), ball.position.y()
            if x - ball.radious < 0 or x + ball.radious > self.width():
                ball.reflect(1)
            if y - ball.radious < 0 or y + ball.radious > self.height():
                ball.reflect(0)
        self.update()
    
    def paintEvent(self, event):
        painter = qtg.QPainter(self)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        
        for ball in self.balls:
        
            painter.setBrush(qtg.QBrush(ball.color))
            painter.drawEllipse(ball.position, ball.radious, ball.radious)
        return super().paintEvent(event)

    def keyPressEvent(self, event):
        key = event.text()
        print(key)
        if key == 'k' or key == 'l':
            self.key_pressed.emit(key)
            print('hello')
        return super().keyPressEvent(event)

    def spin(self, key):
        print(key)
        if key == 'k':
            for ball in self.balls:
                ball.reflect(0)
        elif key == 'l':
            for ball in self.balls:
                ball.reflect(1)
    
if __name__ == '__main__':
    ...