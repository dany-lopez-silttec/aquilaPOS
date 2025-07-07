# This Python file uses the following encoding: utf-8
import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication

from ui_main import Ui_MainWindow

class MainWindow(PySide6.QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    # Prints PySide6 version
    print(PySide6.__version__)

    # Prints the Qt version used to compile PySide6
    print(PySide6.QtCore.__version__)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    res = app.exec()
    print(res)
    sys.exit(res)
