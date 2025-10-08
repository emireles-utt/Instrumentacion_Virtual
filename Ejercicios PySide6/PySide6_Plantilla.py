import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ventana_ui import Ui_MainWindow

class MiFormulario(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MiFormulario()
    w.show()
    sys.exit(app.exec())