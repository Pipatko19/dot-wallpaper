import sys
import random

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from ball import Ball, Atractor

BALL_RADIUS = 15
OFFSET = BALL_RADIUS + 10
BALL_COUNT = 200
BALL_SPEED = 5

class Wallpaper(qtw.QWidget):
    key_pressed = qtc.Signal(str)
    def __init__(self, geometry: qtc.QRect):
        """Wallpaper constructor"""
        super().__init__()
        self.setGeometry(geometry)
        #Main UI code goes here
        
        self.objects = []

        self.balls = [
            Ball(
                x=random.randint(OFFSET, self.width() - OFFSET),
                y=random.randint(OFFSET, self.height() - OFFSET),
                speed=random.choice([-BALL_SPEED, BALL_SPEED]),
                angle=random.randint(0, 359),
                color=qtg.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 180),
                radius = BALL_RADIUS
            )
            for _ in range(BALL_COUNT)
            ]
        
        self.cursor_ball = Atractor()
        self.objects.extend(self.balls)
        self.objects.append(self.cursor_ball)
        
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.start(30)
        
        self.key_pressed.connect(self.spin)
        #End main UI code
        self.show()
    
    def _update_ball_positions(self):
        for ball in self.balls:
            ball.update()
            x, y = ball.position.x(), ball.position.y()
            if x - ball.radius < 0 or x + ball.radius > self.width():
                ball.reflect(1)
            if y - ball.radius < 0 or y + ball.radius > self.height():
                ball.reflect(0)
    
    def _update_cursor(self):
        new_pos = self.mapFromGlobal(qtg.QCursor.pos())
        self.cursor_ball.update(new_pos)
    
    def update_all(self):
        self._update_ball_positions()
        self._update_cursor()
        self.update()
    
    
    def paintEvent(self, event):
        painter = qtg.QPainter(self)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        
        for obj in self.objects:
            obj.draw(painter)
        
        return super().paintEvent(event)

    def keyPressEvent(self, event):
        key = event.text()
        print(key)
        if key == 'k' or key == 'l':
            self.key_pressed.emit(key)
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