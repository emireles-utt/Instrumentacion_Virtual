import sys
from PySide6.QtWidgets import QDialog, QApplication
from PySide6.QtCore import QTimer
from serialVentana import *
import serial
import time

class MiFormulario(QDialog):
    __ser = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.cmdSalir.clicked.connect(self.salir)
        self.ui.chbSalida.stateChanged.connect(self.salida)

        try:
            self.__ser = serial.Serial()
            self.__ser.port = "COM8"           #cambiar el COM correspondiente
            self.__ser.baudrate = 115200
            #self.__ser.setDTR(False)
            self.__ser.open()
            time.sleep(1.8)
            print("Puerto abierto")
        except serial.serialutil.SerialException:
            print("Error al abrir el puerto")
        else:
            self.timer = QTimer()
            self.timer.start(50)
            self.timer.timeout.connect(self.leerSerial)

    def salida(self):
        try:
            if self.ui.chbSalida.isChecked():
                self.__ser.write(b'A')
            else:
                self.__ser.write(b'a')
        except serial.serialutil.SerialTimeoutException:
            print("Error en el puerto")
            self.close()

    def leerSerial(self):
        try:
            self.__ser.write(b'H')
            datoAdc = self.__ser.readline()
            datoAdc = int(datoAdc.decode("utf-8"))
            self.ui.lblAdc.setText(str(datoAdc))

            if self.ui.chbEntrada.isChecked():
                self.__ser.write(b'1')
                btn0 = self.__ser.read(1)
                self.ui.lblEntrada.setText(btn0.decode("utf-8"))
        except serial.serialutil.SerialTimeoutException:
            print("Error en el puerto")
            self.close()

    def salir(self):
        try:
            self.timer.stop()
            self.__ser.close()
            print("Puerto Cerrado")
        except serial.serialutil.SerialTimeoutException:
            print("Error en el puerto")
        except AttributeError:
            pass
        finally:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    v = MiFormulario()
    v.show()
    sys.exit(app.exec())
