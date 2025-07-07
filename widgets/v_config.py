from PySide6 import QtWidgets

from utils import config, logger
from ui.ui_config import Ui_Config

class VConfig(QtWidgets.QDialog, Ui_Config):
    def __init__(self):
        super(VConfig, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Aquila POS - Configuración")
        #self.setWindowIcon(config.get_icono())

        # Connect the save button to the save method
        #self.btn_save.clicked.connect(self.save)

        # Set the focus on the first field
        #self.txtField1.setFocus()  # Replace with your actual field name