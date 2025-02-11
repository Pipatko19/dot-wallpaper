from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget()
window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_TranslucentBackground)
window.setAttribute(Qt.WA_TransparentForMouseEvents)  # Disables interaction
window.setGeometry(100, 100, 800, 600)  # Set desired window size and position
window.show()

app.exec()
