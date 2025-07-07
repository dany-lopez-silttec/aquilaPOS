# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
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
    QLabel, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(640, 480)
        self.verticalLayout = QVBoxLayout(Config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblTitle = QLabel(Config)
        self.lblTitle.setObjectName(u"lblTitle")

        self.verticalLayout.addWidget(self.lblTitle)

        self.txtConfig = QPlainTextEdit(Config)
        self.txtConfig.setObjectName(u"txtConfig")

        self.verticalLayout.addWidget(self.txtConfig)

        self.buttonBox = QDialogButtonBox(Config)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Config)
        self.buttonBox.accepted.connect(Config.accept)
        self.buttonBox.rejected.connect(Config.reject)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"Dialog", None))
        self.lblTitle.setText(QCoreApplication.translate("Config", u"Configuraciones b\u00e1sicas", None))
    # retranslateUi

