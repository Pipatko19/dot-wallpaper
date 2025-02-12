import sys
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg
from PySide6 import QtCore as qtc
from wallpaper import Wallpaper

class MainWindow(qtw.QMainWindow):
    
    def __init__(self, geometry: qtc.QRect = qtc.QRect(50, 50, 50, 50)):
        """MainWindow constructor"""
        super().__init__()
        self.setWindowTitle('Wallpaper')
        
        #self.setWindowFlags(qtc.Qt.FramelessWindowHint | qtc.Qt.WindowStaysOnTopHint)
        self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.setAttribute(qtc.Qt.WA_TransparentForMouseEvents)
        self.setGeometry(geometry)

        self.animated_wallpaper = Wallpaper(geometry)
        self.setCentralWidget(self.animated_wallpaper)

        
        self.centralWidget().setFocus()
        
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    screen = app.primaryScreen()
    screen_geometry = screen.availableGeometry()
    mw = MainWindow(screen_geometry)
    sys.exit(app.exec())