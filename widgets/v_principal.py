from PySide6 import QtWidgets

from utils import config, logger
from ui.ui_principal import Ui_Principal

class VPrincipal(QtWidgets.QMainWindow, Ui_Principal):
    def __init__(self):
        super(VPrincipal, self).__init__()
        self.setupUi(self)