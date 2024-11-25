# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficacvGaiU.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QWidget)

from pyqtgraph import PlotWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(605, 546)
        self.graphWidget = PlotWidget(Dialog)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(9, 9, 591, 441))
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 470, 591, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cmdConectar = QPushButton(self.horizontalLayoutWidget)
        self.cmdConectar.setObjectName(u"cmdConectar")

        self.horizontalLayout.addWidget(self.cmdConectar)

        self.cmdSalir = QPushButton(self.horizontalLayoutWidget)
        self.cmdSalir.setObjectName(u"cmdSalir")

        self.horizontalLayout.addWidget(self.cmdSalir)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cmdConectar.setText(QCoreApplication.translate("Dialog", u"CONECTAR", None))
        self.cmdSalir.setText(QCoreApplication.translate("Dialog", u"SALIR", None))
    # retranslateUi

