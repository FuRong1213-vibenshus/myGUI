import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QPushButton, 
                               QHBoxLayout,
                               QVBoxLayout,
                               QWidget)

from layout_colorwidget import Color

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        layout2.addWidget(Color('red')) 
        layout2.addWidget(Color('yellow')) 
        layout2.addWidget(Color('purple')) 

        layout1.addLayout(layout2) 

        layout1.addWidget(Color('green')) 
        layout3.addWidget(Color('purple')) 
        layout1.addLayout(layout3)        

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
