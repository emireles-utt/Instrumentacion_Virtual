# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serialWkYmVU.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(154, 152)
        self.cmdSalir = QPushButton(Dialog)
        self.cmdSalir.setObjectName(u"cmdSalir")
        self.cmdSalir.setGeometry(QRect(10, 110, 111, 23))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.cmdSalir.setFont(font)
        self.chbEntrada = QCheckBox(Dialog)
        self.chbEntrada.setObjectName(u"chbEntrada")
        self.chbEntrada.setGeometry(QRect(10, 80, 87, 23))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.chbEntrada.setFont(font1)
        self.lblEntrada = QLabel(Dialog)
        self.lblEntrada.setObjectName(u"lblEntrada")
        self.lblEntrada.setGeometry(QRect(100, 80, 91, 19))
        self.lblEntrada.setFont(font1)
        self.chbSalida = QCheckBox(Dialog)
        self.chbSalida.setObjectName(u"chbSalida")
        self.chbSalida.setGeometry(QRect(10, 50, 73, 23))
        self.chbSalida.setFont(font1)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 41, 19))
        self.label.setFont(font1)
        self.lblAdc = QLabel(Dialog)
        self.lblAdc.setObjectName(u"lblAdc")
        self.lblAdc.setGeometry(QRect(60, 20, 71, 19))
        self.lblAdc.setFont(font1)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cmdSalir.setText(QCoreApplication.translate("Dialog", u"Salir", None))
        self.chbEntrada.setText(QCoreApplication.translate("Dialog", u"Entrada", None))
        self.lblEntrada.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.chbSalida.setText(QCoreApplication.translate("Dialog", u"Salida", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ADC:", None))
        self.lblAdc.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

