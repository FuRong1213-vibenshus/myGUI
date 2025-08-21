import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
            
        self.setMouseTracking(True)
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.label.setMouseTracking(True)

    def mousePressEvent(self, e):
        #self.label.setText("mouseMoveEvent")
        if e.button() == Qt.MouseButton.LeftButton:

            self.label.setText("Left")
        elif e.button() == Qt.MouseButton.RightButton:

            self.label.setText("Right")

    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
