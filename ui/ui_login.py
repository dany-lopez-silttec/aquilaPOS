# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from resources import rc_resources

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(585, 272)
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblImg = QLabel(self.widget)
        self.lblImg.setObjectName(u"lblImg")
        self.lblImg.setMinimumSize(QSize(100, 100))
        self.lblImg.setMaximumSize(QSize(200, 200))
        self.lblImg.setPixmap(QPixmap(u":/img/aquila_logo.svg"))
        self.lblImg.setScaledContents(True)
        self.lblImg.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblImg)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.formLayout = QFormLayout(self.widget_2)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(0, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)

        self.lblUser = QLabel(self.widget_2)
        self.lblUser.setObjectName(u"lblUser")
        font = QFont()
        font.setPointSize(16)
        self.lblUser.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblUser)

        self.txtUser = QLineEdit(self.widget_2)
        self.txtUser.setObjectName(u"txtUser")
        self.txtUser.setMinimumSize(QSize(200, 0))
        self.txtUser.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtUser)

        self.lblPass = QLabel(self.widget_2)
        self.lblPass.setObjectName(u"lblPass")
        self.lblPass.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPass)

        self.txtPass = QLineEdit(self.widget_2)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setFont(font)
        self.txtPass.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txtPass)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.ItemRole.FieldRole, self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(Login)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Login)
        self.buttonBox.accepted.connect(Login.accept)
        self.buttonBox.rejected.connect(Login.reject)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.lblImg.setText("")
        self.lblUser.setText(QCoreApplication.translate("Login", u"Usuario:", None))
        self.lblPass.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a:", None))
    # retranslateUi

