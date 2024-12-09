import sys
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from ui_consulta import Ui_Dialog


class MiFormulario(QDialog, Ui_Dialog):
    alumnos = {}                                # diccionario donde almacenamos alumnos y calificaciones

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.cmdAgregar.clicked.connect(self.agregarDiccionario)
        self.cmdConsultar.clicked.connect(self.consultarDiccionario)
        self.cmdCalcular1.clicked.connect(self.promedioAlumno)
        self.cmdCalcular2.clicked.connect(self.promedioUnidad)
        self.cmdCalcular3.clicked.connect(self.promedioGrupo)
    '''
    Esta funcion agrega un nuevo alumno y sus calificaciones al diccionario
    '''
    def agregarDiccionario(self):
        # verificamos si los LineEdit tienen algo antes de pasarlos al diccionario
        if self.lineNombre.text() != "" and self.lineCUnidad1.text() != "" and self.lineCUnidad2.text() != "" and self.lineCUnidad3.text() != "":
            nombre = self.lineNombre.text()                 # tomamos el nombre del alumno
            if nombre not in self.alumnos:                  # verificamos si el nombre esta en el diccionario
                calif1 = int(self.lineCUnidad1.text())      # si no esta capturamos las calificaciones
                calif2 = int(self.lineCUnidad2.text())
                calif3 = int(self.lineCUnidad3.text())

                lista = [calif1, calif2, calif3]            # creamos una lista con las calificaciones
                self.alumnos[nombre] = lista                # agregamos el nombre y las calificaciones al diccionario
                print(self.alumnos)                         # imprimimos el contenido del diccionario
            else:
                # si el alumno esta en el diccionario mandamos un mensaje de advertencia
                QMessageBox.question(self, "Error", "El alumno ya esta en la lista", QMessageBox.Ok)
        else:
            # si algun LineEdit no tiene datos mandamos un mensaje de error
            QMessageBox.question(self, "Error", "Datos Invalidos", QMessageBox.Ok)
        # borramos los LineEdit del nombnre y calificaciones
        self.lineNombre.clear()
        self.lineCUnidad1.clear()
        self.lineCUnidad2.clear()
        self.lineCUnidad3.clear()

    '''
    Esta funcion realiza la consulta del diccionario por nombre del alumno y muestra sus calificaciones
    '''
    def consultarDiccionario(self):
        if self.lineConsultar.text() != "":                 # verificamos si el LineEdit tiene un nombre valido
            nombre = self.lineConsultar.text()              # tomamos el nombre del LineEdit
            if nombre in self.alumnos:                      # si el alumno esta en el diccionario
                lista = self.alumnos[nombre]                # tomamos las califcaciones y las almacenamos en una lista

                # desplegamos las calificaciones en el LineEdit correspondiente
                self.lineUnidad1.setText(str(lista[0]))
                self.lineUnidad2.setText(str(lista[1]))
                self.lineUnidad3.setText(str(lista[2]))
            else:
                # si el alumno no existe en el diccionario mandamos un mensaje de error
                QMessageBox.question(self, "Error", "Alumno no existe", QMessageBox.Ok)
        else:
            # si el LineEdit no cotienen un valor valido mandamos un mensajes de error
            QMessageBox.question(self, "Error", "Datos Invalidos", QMessageBox.Ok)

    '''
    Esta funcion calcula el promedio por alumno.
    '''
    def promedioAlumno(self):
        if self.lineCalNombre.text() != "":         # verificamos si el LineEdit tiene un nombre valido
            nombre = self.lineCalNombre.text()      # tomamos el nombre del LineEdit
            if nombre in self.alumnos:              # verificamos si el alumno esta en el diccionario
                lista = self.alumnos[nombre]        # sacmos las calificaciones del alumno y las almacenamos en una lista
                prom = sum(lista) / 3               # calculamos el promedio sumando las tres calificaciones y diviendolas entre tres
                self.linePromedio1.setText("{:.2f}".format(prom))   # desplegamos el promedio en el LineEdit
            else:
                # si el alumno no existe en el diccionario mandamos un mensaje de error
                QMessageBox.question(self, "Error", "Alumno no existe", QMessageBox.Ok)
        else:
            # si el LineEdit no cotienen un valor valido mandamos un mensajes de error
            QMessageBox.question(self, "Error", "Datos Invalidos", QMessageBox.Ok)

    '''
    Esta funcion calcula el promedio por unidad seleccionada.
    '''
    def promedioUnidad(self):
        lista = []

        # checamos si se desea calcular el promedio de la unidad 1
        if self.chkUnidad1.isChecked():
            acc = 0                 # acumulador de calificaciones de la unidad 1
            numAlumnos = 0          # numero de alumnos de esta unidad

            # leemos las calificaciones de los alumnos con el metodo keys
            for i in self.alumnos.keys():
                lista = self.alumnos[i]     # guardamos las calificaciones en una lista temporal
                acc += lista[0]             # sumamos unicamente las calificaciones de la unidad 1
                numAlumnos += 1             # incrementamos el contador de alumnos de la unidad 1
            # calculamos el promedio por unidad con la suma de las calificaciones de la unidad 1 entre el numero de alumnos
            # desplegamos el promedio en el LineEdit
            self.linePromUn1.setText("{:.2f}".format(acc / numAlumnos))

        # checamos si se desea calcular el promedio de la unidad 2
        if self.chkUnidad2.isChecked():
            acc = 0                         # acumulador de calificaciones de la unidad 2
            numAlumnos = 0                  # numero de alumnos de esta unidad

            # leemos las calificaciones de los alumnos con el metodo keys
            for i in self.alumnos.keys():
                lista = self.alumnos[i]     # guardamos las calificaciones en una lista temporal
                acc += lista[1]             # sumamos unicamente las calificaciones de la unidad 2
                numAlumnos += 1             # incrementamos el contador de alumnos de la unidad 2
            # calculamos el promedio por unidad con la suma de las calificaciones de la unidad 2 entre el numero de alumnos
            # desplegamos el promedio en el LineEdit
            self.linePromUn2.setText("{:.2f}".format(acc / numAlumnos))

        # checamos si se desea calcular el promedio de la unidad 3
        if self.chkUnidad3.isChecked():
            acc = 0                         # acumulador de calificaciones de la unidad 3
            numAlumnos = 0                  # numero de alumnos de esta unidad

            # leemos las calificaciones de los alumnos con el metodo keys
            for i in self.alumnos.keys():
                lista = self.alumnos[i]     # guardamos las calificaciones en una lista temporal
                acc += lista[2]             # sumamos unicamente las calificaciones de la unidad 3
                numAlumnos += 1             # incrementamos el contador de alumnos de la unidad 3
            # calculamos el promedio por unidad con la suma de las calificaciones de la unidad 3 entre el numero de alumnos
            # desplegamos el promedio en el LineEdit
            self.linePromUn3.setText("{:.2f}".format(acc / numAlumnos))

    '''
    Esta funcion calcula el promedio de todo el grupo.
    '''
    def promedioGrupo(self):
        acc = [0, 0, 0]                                 # acumulador de calificaciones
        promUnidad = [0, 0, 0]                          # acumulador de promedios por unidad

        # checamos si tenemos datos en el diccionario
        if len(self.alumnos) != 0:
            for i in self.alumnos.keys():               # leemos las calificaciones por alumno
                lista = self.alumnos[i]                 # almacenamos las calificaciones en una lista temporal
                for x in range(0, 3):
                    acc[x] += lista[x]                  # realizamos la suma de las calificaciones por unidad
            promUnidad[0] = acc[0] / len(self.alumnos)  # calculamos el promedio de la unidad 1
            promUnidad[1] = acc[1] / len(self.alumnos)  # calculamos el promedio de la unidad 2
            promUnidad[2] = acc[2] / len(self.alumnos)  # calculamos el promedio de la unidad 3
            # calculamos el promedio de las tres unidades de todo el grupo
            accTotal = (promUnidad[0] + promUnidad[1] + promUnidad[2]) / 3
            # desplegamos el promedio en el LineEdit
            self.linePromGrupo.setText("{:.2f}".format(accTotal))
        else:
            # si no hay datos en el diccionario enviamos un mensaje de error
            QMessageBox.question(self, "Error", "No hay capturas", QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MiFormulario()
    w.show()
    sys.exit(app.exec())
