import sys
from PySide6.QtWidgets import QGridLayout, QApplication, QMainWindow, QWidget
from tictactoe import TicTacToe
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        layout = QGridLayout()
        for row in range(3):
            for col in range(3):
                layout.addWidget( TicTacToe(), row, col)
        
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)