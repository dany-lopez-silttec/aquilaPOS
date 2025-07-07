from PySide6 import QtWidgets

from utils import config, logger
from ui.ui_login import Ui_Login

class VLogin(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super(VLogin, self).__init__()
        self.setupUi(self)
        
        self.setWindowTitle("Aquila POS - Login")
        #self.setWindowIcon(config.get_icono())
        
        # Connect the login button to the login method
        #self.btn_login.clicked.connect(self.login)
        
        # Set the focus on the username field
        self.txtUser.setFocus()