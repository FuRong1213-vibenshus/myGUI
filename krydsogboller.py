import sys
from PySide6.QtCore import QAbstractTableModel, Qt

from mainwindow_3_ui import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QTableView, 
                               QVBoxLayout, 
                               QWidget, 
                               QHBoxLayout, 
                               QLineEdit, 
                               QTextEdit)

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
    
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table = QTableView()
        data = [[4, 1, 3, 3, 7], [9, 1, 5, 3, 8], [2, 1, 5, 3, 9]]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.tabl)

# loader = QUiLoader()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.setStyle('Fusion')
#dialog = loader.load("mainwindow_opgave2.ui", None)
#dialog.show()
app.exec()