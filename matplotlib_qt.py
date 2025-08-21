import sys

import numpy as np

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.figure import Figure

from PySide6.QtWidgets import (QApplication, 
                               QMainWindow, 
                               QPushButton, 
                               QHBoxLayout,
                               QVBoxLayout,
                               QWidget,
                               QLineEdit,
                               QLabel)


        

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.coeffs = []
        self._main = QWidget()
        self.setCentralWidget(self._main)
        layout_main = QVBoxLayout(self._main)
        layout_abc =  QHBoxLayout()
        
        self.static_canvas = FigureCanvas(Figure(figsize=(5,3)))
        layout_main.addWidget(NavigationToolbar(self.static_canvas, self))

        self.coeff_a = QLineEdit()
        self.coeff_b = QLineEdit()
        self.coeff_c = QLineEdit()
        self.startButton = QPushButton("Calculate")
        self.roots_text = QLineEdit()
        self.roots_text.setVisible(False)
        self.roots_text.setReadOnly(True)
        self.coeff_a.setPlaceholderText("1")
        self.coeff_b.setPlaceholderText("0")
        self.coeff_c.setPlaceholderText("0")
        layout_abc.addWidget(self.coeff_a)
        layout_abc.addWidget(self.coeff_b)
        layout_abc.addWidget(self.coeff_c)
        layout_abc.addWidget(self.startButton)
        layout_main.addLayout(layout_abc)
        layout_main.addWidget(self.roots_text)
        layout_main.addWidget(self.static_canvas)
        self._static_ax = self.static_canvas.figure.subplots()
        

        #connect signals and slots

        self.startButton.clicked.connect(self.update_result)
        self.roots_text.textChanged.connect(self.update_plot)

    def update_result(self):

        self.coeffs = [float(x) for x in [self.coeff_a.text(), self.coeff_b.text(), self.coeff_c.text()]]
        
        self.roots_text.setVisible(True)
        self.roots = np.roots(self.coeffs)


        self.roots_text.setText(str(self.roots)) 
    
    def update_plot(self):
        a, b, c = self.coeffs[0], self.coeffs[1], self.coeffs[2]
        self._static_ax.cla()
        x = np.linspace(-4, 2, 501)
        self._static_ax.axhline(0, color='k', ls='--', lw=1)
        self._static_ax.plot(x, a*x**2+b*x+c, ".")
        self._static_ax.plot(self.roots, np.repeat(0, self.roots.size), 'o', label = 'roots')
        self._static_ax.grid(True)
        self.static_canvas.draw()
    

if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()