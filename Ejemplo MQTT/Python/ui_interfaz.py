# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazhMabNg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 206)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cmdSalir = QPushButton(self.centralwidget)
        self.cmdSalir.setObjectName(u"cmdSalir")
        self.cmdSalir.setGeometry(QRect(280, 130, 75, 31))
        font = QFont()
        font.setBold(True)
        self.cmdSalir.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 51, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.btnLed = QPushButton(self.centralwidget)
        self.btnLed.setObjectName(u"btnLed")
        self.btnLed.setGeometry(QRect(80, 130, 75, 31))
        self.btnLed.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 71, 31))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 47, 31))
        self.label_3.setFont(font1)
        self.lblBoton = QLabel(self.centralwidget)
        self.lblBoton.setObjectName(u"lblBoton")
        self.lblBoton.setGeometry(QRect(110, 70, 31, 31))
        self.lblBoton.setFont(font1)
        self.barAdc = QProgressBar(self.centralwidget)
        self.barAdc.setObjectName(u"barAdc")
        self.barAdc.setGeometry(QRect(80, 10, 311, 31))
        self.barAdc.setMaximum(4095)
        self.barAdc.setValue(0)
        self.cmdConectar = QPushButton(self.centralwidget)
        self.cmdConectar.setObjectName(u"cmdConectar")
        self.cmdConectar.setGeometry(QRect(180, 130, 75, 31))
        self.cmdConectar.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cmdSalir.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ADC:", None))
        self.btnLed.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BOTON:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LED:", None))
        self.lblBoton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cmdConectar.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
    # retranslateUi

