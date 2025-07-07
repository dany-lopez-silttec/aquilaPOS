# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_Principal(object):
    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.resize(930, 688)
        self.centralwidget = QWidget(Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.w_principal = QWidget(self.centralwidget)
        self.w_principal.setObjectName(u"w_principal")

        self.horizontalLayout.addWidget(self.w_principal)

        self.w_botones = QWidget(self.centralwidget)
        self.w_botones.setObjectName(u"w_botones")
        self.w_botones.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout = QVBoxLayout(self.w_botones)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.w_botones)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.w_botones)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.w_botones)

        Principal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 930, 23))
        Principal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Principal)
        self.statusbar.setObjectName(u"statusbar")
        Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Principal)

        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(QCoreApplication.translate("Principal", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("Principal", u"Boton 1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Principal", u"Boton2", None))
    # retranslateUi

