# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the Qt Designer taskmenuextension example from Qt v6.x"""

import sys
from PySide6.QtWidgets import QApplication

from tictactoe import TicTacToe
from mainwindow import MainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    #window.state = "---------"
    print("You are calling me!!")
    window.show()
    sys.exit(app.exec())