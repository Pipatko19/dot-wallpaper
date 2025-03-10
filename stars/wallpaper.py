import random

from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc

from ball import Ball
from functions import average_colors

BALL_RADIUS = 15
OFFSET = BALL_RADIUS + 10
BALL_COUNT = 100
BALL_SPEED = 8

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
                speed=BALL_SPEED,
                angle=random.randint(0, 359),
                color=qtg.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 180),
                radius = BALL_RADIUS
            )
            for _ in range(BALL_COUNT)
            ]

        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.update_all)
        self.timer.start(30)
        
        self.key_pressed.connect(self.spin)
        #End main UI code
        
        self.show()
    
    def update_ball_positions(self):
        for ball in self.balls:
            ball.update()
            x, y = ball.position.x(), ball.position.y()
            if x - ball.radius < 0 or x + ball.radius > self.width():
                ball.reflect(1)
            if y - ball.radius < 0 or y + ball.radius > self.height():
                ball.reflect(0)
    
    def find_lines(self):
        lines = []
        seen_balls = set()
        for ball in self.balls:
            min_distance = float('inf')
            closest_ball = None
            for other_ball in self.balls:
                if ball is other_ball or ball in seen_balls:
                    continue
                dist = ball.position.distanceToPoint(other_ball.position)
                if min_distance > dist:
                    min_distance = dist
                    closest_ball = other_ball
            if closest_ball is not None: 
                lines.append((qtc.QLineF(ball.point, closest_ball.point), 
                             average_colors(ball.color, closest_ball.color)))
                seen_balls.add(closest_ball)
        return lines
    
    def update_all(self):
        self.update_ball_positions()
        self.update()
    
    def draw_lines(self, painter: qtg.QPainter, lines: list[tuple[qtc.QLineF, qtg.QColor]]):
        for line, color in lines:
            h, s, v, a = color.getHsv()
            color = qtg.QColor.fromHsv(h, s, min(255, v + 70), 255)
            pen = qtg.QPen(color, 2)
            painter.setPen(pen)
            painter.drawLine(line)
    
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = qtg.QPainter(self)
        painter.setRenderHint(qtg.QPainter.Antialiasing)
        
        for obj in self.balls:
            obj.draw(painter)
            
        self.draw_lines(painter, self.find_lines())
        
        painter.end()

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