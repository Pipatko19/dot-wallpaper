import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc

def average_colors(color1: qtg.QColor, color2: qtg.QColor) -> qtg.QColor:
    """Returns the average color between two QColor objects."""
    r = (color1.red() + color2.red()) // 2
    g = (color1.green() + color2.green()) // 2
    b = (color1.blue() + color2.blue()) // 2
    a = (color1.alpha() + color2.alpha()) // 2  # Include alpha for transparency

    return qtg.QColor(r, g, b, a)