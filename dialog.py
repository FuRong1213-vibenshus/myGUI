import sys
from PySide6.QtWidgets import (QApplication, 
                               QDialog, 
                               QLineEdit, 
                               QPushButton,
                               QVBoxLayout,
                               )

class Form(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Form")

        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print(f"Hello {self.edit.text()}")
        self.button.setText(f"Hello {self.edit.text()}")

if __name__ == '__main__':
    # Crate the Qt Application
    app = QApplication(sys.argv)
    # Create an dhow the form±±++

    form = Form()
    form.show()

    #Run the main Qt loop
    sys.exit(app.exec())