import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_interfaz import Ui_MainWindow
import paho.mqtt.client as mqtt


class MiVentan(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLed.clicked.connect(self.toogleLed)
        self.cmdConectar.clicked.connect(self.conectar)
        self.cmdSalir.clicked.connect(self.salir)

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe("esp32/adc", qos=2)
        self.client.subscribe("esp32/boton", qos=2)
        print("Suscrito")

    def on_message(self, client, userdata, msg):
        if msg.topic == "esp32/adc":
            datoAdc = str(msg.payload.decode("utf-8"))
            datoAdc = int(datoAdc)
            self.barAdc.setValue(datoAdc)
        elif msg.topic == "esp32/boton":
            datoBoton = str(msg.payload.decode("utf-8"))
            self.lblBoton.setText(datoBoton)

    def toogleLed(self):
        if self.btnLed.text() == "ON":
            self.btnLed.setText("OFF")
            self.client.publish("esp32/led", "ON")
        else:
            self.btnLed.setText("ON")
            self.client.publish("esp32/led", "OFF")

    def conectar(self):
        self.client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
        self.client.loop_start()

    def salir(self):
        try:
            self.client.unsubscribe("esp32/adc")
            self.client.unsubscribe("esp32/boton")
        except:
            print("Fallo al desconectar")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    venta = MiVentan()
    venta.show()
    sys.exit(app.exec())