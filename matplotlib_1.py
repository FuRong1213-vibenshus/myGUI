import os
import sys

os.environ["QT_API"] = "PySide6"

from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QLineEdit

from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        toolbar = NavigationToolbar(self.canvas, self)

        layout_main = QVBoxLayout()
        layout_main.addWidget(toolbar)
        layout_main.addWidget(self.canvas)
        
        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QWidget()        
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)
        
        
        self.coeffs = []
        layout_abc =  QHBoxLayout()


        self.coeff_a = QLineEdit()
        self.coeff_b = QLineEdit()
        self.coeff_c = QLineEdit()
        self.startButton = QPushButton("Calculate")
        self.roots_text = QLineEdit()
        self.roots_text.setVisible(False)
        self.roots_text.setReadOnly(True)
        self.coeff_a.setPlaceholderText("a")
        self.coeff_b.setPlaceholderText("b")
        self.coeff_c.setPlaceholderText("c")
        layout_abc.addWidget(self.coeff_a)
        layout_abc.addWidget(self.coeff_b)
        layout_abc.addWidget(self.coeff_c)
        layout_abc.addWidget(self.startButton)
        layout_main.addLayout(layout_abc)
        layout_main.addWidget(self.roots_text)
        #self._static_ax = sc.axes

        #self._static_ax = self.static_canvas.figure.subplots()
        # Create a placeholder widget to hold our toolbar and canvas.

        
        self.startButton.clicked.connect(self.update_result)
        self.roots_text.textChanged.connect(self.update_plot)

    def update_result(self):

        self.coeffs = [float(x) for x in [self.coeff_a.text(), self.coeff_b.text(), self.coeff_c.text()]]
        
        self.roots_text.setVisible(True)
        self.roots = np.roots(self.coeffs)


        self.roots_text.setText(str(self.roots)) 
    
    def update_plot(self):
        a, b, c = self.coeffs[0], self.coeffs[1], self.coeffs[2]
        self.canvas.axes.cla()
        x = np.linspace(-4, 2, 501)
        self.canvas.axes.axhline(0, color='k', ls='--', lw=1)
        self.canvas.axes.plot(x, a*x**2+b*x+c, ".")
        self.canvas.axes.plot(self.roots, np.repeat(0, self.roots.size), 'o', label = 'roots')
        self.canvas.axes.grid(True)
        self.canvas.draw()

if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(sys.argv)

    app = MainWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec()
