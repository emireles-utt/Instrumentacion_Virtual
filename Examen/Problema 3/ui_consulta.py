# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consultaoqopcL.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(773, 407)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 751, 391))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(210, 90, 351, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineCUnidad2 = QLineEdit(self.gridLayoutWidget)
        self.lineCUnidad2.setObjectName(u"lineCUnidad2")

        self.gridLayout.addWidget(self.lineCUnidad2, 2, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineCUnidad3 = QLineEdit(self.gridLayoutWidget)
        self.lineCUnidad3.setObjectName(u"lineCUnidad3")

        self.gridLayout.addWidget(self.lineCUnidad3, 3, 1, 1, 1)

        self.lineNombre = QLineEdit(self.gridLayoutWidget)
        self.lineNombre.setObjectName(u"lineNombre")

        self.gridLayout.addWidget(self.lineNombre, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineCUnidad1 = QLineEdit(self.gridLayoutWidget)
        self.lineCUnidad1.setObjectName(u"lineCUnidad1")

        self.gridLayout.addWidget(self.lineCUnidad1, 1, 1, 1, 1)

        self.cmdAgregar = QPushButton(self.tab)
        self.cmdAgregar.setObjectName(u"cmdAgregar")
        self.cmdAgregar.setGeometry(QRect(210, 260, 351, 41))
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 40, 211, 31))
        self.label_5.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 741, 131))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 40, 301, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout.addWidget(self.label_6)

        self.lineConsultar = QLineEdit(self.horizontalLayoutWidget)
        self.lineConsultar.setObjectName(u"lineConsultar")

        self.horizontalLayout.addWidget(self.lineConsultar)

        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(360, 40, 361, 57))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineUnidad2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineUnidad2.setObjectName(u"lineUnidad2")
        self.lineUnidad2.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineUnidad2, 1, 1, 1, 1)

        self.lineUnidad3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineUnidad3.setObjectName(u"lineUnidad3")
        self.lineUnidad3.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineUnidad3, 1, 2, 1, 1)

        self.lineUnidad1 = QLineEdit(self.gridLayoutWidget_2)
        self.lineUnidad1.setObjectName(u"lineUnidad1")
        self.lineUnidad1.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineUnidad1, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)

        self.cmdConsultar = QPushButton(self.groupBox)
        self.cmdConsultar.setObjectName(u"cmdConsultar")
        self.cmdConsultar.setGeometry(QRect(20, 100, 301, 23))
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 150, 741, 201))
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 40, 221, 151))
        self.formLayoutWidget = QWidget(self.groupBox_3)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 201, 31))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.lineCalNombre = QLineEdit(self.formLayoutWidget)
        self.lineCalNombre.setObjectName(u"lineCalNombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineCalNombre)

        self.cmdCalcular1 = QPushButton(self.groupBox_3)
        self.cmdCalcular1.setObjectName(u"cmdCalcular1")
        self.cmdCalcular1.setGeometry(QRect(10, 120, 201, 23))
        self.linePromedio1 = QLineEdit(self.groupBox_3)
        self.linePromedio1.setObjectName(u"linePromedio1")
        self.linePromedio1.setEnabled(False)
        self.linePromedio1.setGeometry(QRect(10, 80, 201, 20))
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(260, 40, 221, 151))
        self.formLayoutWidget_2 = QWidget(self.groupBox_4)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 20, 191, 95))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.chkUnidad1 = QCheckBox(self.formLayoutWidget_2)
        self.chkUnidad1.setObjectName(u"chkUnidad1")
        self.chkUnidad1.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.chkUnidad1)

        self.chkUnidad2 = QCheckBox(self.formLayoutWidget_2)
        self.chkUnidad2.setObjectName(u"chkUnidad2")
        self.chkUnidad2.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.chkUnidad2)

        self.chkUnidad3 = QCheckBox(self.formLayoutWidget_2)
        self.chkUnidad3.setObjectName(u"chkUnidad3")
        self.chkUnidad3.setFont(font1)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.chkUnidad3)

        self.linePromUn1 = QLineEdit(self.formLayoutWidget_2)
        self.linePromUn1.setObjectName(u"linePromUn1")
        self.linePromUn1.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.linePromUn1)

        self.linePromUn2 = QLineEdit(self.formLayoutWidget_2)
        self.linePromUn2.setObjectName(u"linePromUn2")
        self.linePromUn2.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.linePromUn2)

        self.linePromUn3 = QLineEdit(self.formLayoutWidget_2)
        self.linePromUn3.setObjectName(u"linePromUn3")
        self.linePromUn3.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.linePromUn3)

        self.cmdCalcular2 = QPushButton(self.groupBox_4)
        self.cmdCalcular2.setObjectName(u"cmdCalcular2")
        self.cmdCalcular2.setGeometry(QRect(20, 120, 191, 23))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(510, 40, 221, 151))
        self.verticalLayoutWidget = QWidget(self.groupBox_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 40, 181, 93))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.linePromGrupo = QLineEdit(self.verticalLayoutWidget)
        self.linePromGrupo.setObjectName(u"linePromGrupo")
        self.linePromGrupo.setEnabled(False)

        self.verticalLayout.addWidget(self.linePromGrupo)

        self.cmdCalcular3 = QPushButton(self.verticalLayoutWidget)
        self.cmdCalcular3.setObjectName(u"cmdCalcular3")

        self.verticalLayout.addWidget(self.cmdCalcular3)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Unidad 2", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Unidad 3", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Unidad 1", None))
        self.cmdAgregar.setText(QCoreApplication.translate("Dialog", u"&Agregar", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Captura de calificaciones", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Captura", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Consulta por nombre", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Unidad 1", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Unidad 2", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Unidad 3", None))
        self.cmdConsultar.setText(QCoreApplication.translate("Dialog", u"Consultar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Calcular promedio", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Por Alumno", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.cmdCalcular1.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Por unidad", None))
        self.chkUnidad1.setText(QCoreApplication.translate("Dialog", u"Unidad 1", None))
        self.chkUnidad2.setText(QCoreApplication.translate("Dialog", u"Unidad 2", None))
        self.chkUnidad3.setText(QCoreApplication.translate("Dialog", u"Unidad 3", None))
        self.cmdCalcular2.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Por grupo", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Promedio grupal", None))
        self.cmdCalcular3.setText(QCoreApplication.translate("Dialog", u"Calcular", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Consulta", None))
    # retranslateUi

