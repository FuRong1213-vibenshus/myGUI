import sys
from PySide6.QtUiTools import QUiLoader

from mainwindow_ui import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QPushButton, 
                               QVBoxLayout, 
                               QWidget, 
                               QHBoxLayout, 
                               QLineEdit, 
                               QTextEdit)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.translate_text)

    def translate_text(self):
        input_str = self.plainTextEdit.toPlainText()
        translated_str = self.roever_translate(input_str)
        self.plainTextEdit_2.setPlainText(translated_str)

    def roever_translate(self, text):
        vowels = "aeiouAEIOU"
        translated = []
        for char in text:
            if char not in vowels:
                translated.append(char + 'o' + char.lower())
            else:
                translated.append(char)
        return ''.join(translated)



# loader = QUiLoader()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.setStyle('Fusion')
#dialog = loader.load("mainwindow_opgave2.ui", None)
#dialog.show()
app.exec()