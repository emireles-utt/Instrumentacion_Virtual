from PySide6.QtWidgets import QDialog, QApplication
from grafica import Ui_Dialog
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import paho.mqtt.client as mqtt
from PySide6.QtCore import QTimer
import sys


class MiFormulario(QDialog, Ui_Dialog):
    datoAdc1 = 0
    datoAdc2 = 0
    dataY = []
    dataX1 = []
    dataX2 = []
    lastY = 0
    line = 0

    def __init__(self):
        super().__init__()
        self.graphWidget = pg.PlotWidget()
        self.setupUi(self)
        self.cmdConectar.clicked.connect(self.conectar)
        self.cmdSalir.clicked.connect(self.salir)
        self.timer = QTimer()
        self.timer.timeout.connect(self.leerDatos)

        self.client = mqtt.Client()
        self.client = mqtt.Client(protocol=mqtt.MQTTv311)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Agregamos color de fondo
        self.graphWidget.setBackground('w')
        # Agregamos etiquietas a los ejes
        self.graphWidget.setLabel('left', 'ADC', color='red', size=30)
        self.graphWidget.setLabel('bottom', 'Tiempo', color='red', size=30)
        # Agregamos los titulos
        self.graphWidget.addLegend()
        # Agregamos cuadricula en el eje X y Y
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setYRange(0, 4096, padding=0)

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("iv/adc1/val", qos=2)
        client.subscribe("iv/adc2/val", qos=2)
        print("Suscrito")

    def on_message(self, client, userdata, msg):
        if msg.topic == "iv/adc1/val":
            self.datoAdc1 = str(msg.payload.decode("utf-8"))
            self.datoAdc1 = int(self.datoAdc1)
        elif msg.topic == "iv/adc2/val":
            self.datoAdc2 = str(msg.payload.decode("utf-8"))
            self.datoAdc2 = int(self.datoAdc2)


    def leerDatos(self):
        self.client.publish("iv/adc1/cmd", "A")
        print(self.datoAdc1)

        self.client.publish("iv/adc2/cmd", "B")
        print(self.datoAdc2)

        # Agregamos los datos al array
        self.dataY.append(self.lastY)
        self.dataX1.append(self.datoAdc1)
        self.dataX2.append(self.datoAdc2)
        self.lastY += 50

        if self.lastY % 100 == 0:
            self.dataY = self.dataY[:-1]
            self.dataX1 = self.dataX1[:-1]
            self.dataX2 = self.dataX2[:-1]

        self.plot(self.dataY, self.dataX1, 'r')
        self.plot(self.dataY, self.dataX2, 'b')

    def plot(self, x, y, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, pen=pen)

    def conectar(self):
        self.client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
        self.client.loop_start()
        self.timer.start(10)

    def salir(self):
        try:
            self.client.unsubscribe("iv/adc1/val")
            self.client.unsubscribe("iv/adc2/val")
        except:
            print("Fallo al desconectar")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MiFormulario()
    w.show()
    sys.exit(app.exec())
