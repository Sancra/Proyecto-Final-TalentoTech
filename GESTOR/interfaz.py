import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog, QDialogButtonBox, QInputDialog
import operaciones_notas as op

class VentanaReclamo(QDialog):
    def __init__(self, estudiante, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Reclamar Nota')
        self.setGeometry(400, 400, 800, 600)

        self.estudiante = estudiante  # Guardar el estudiante recibido como atributo

        self.layout = QVBoxLayout(self)

        self.label_materia = QLabel('Materia:')
        self.input_materia = QLineEdit()
        self.layout.addWidget(self.label_materia)
        self.layout.addWidget(self.input_materia)

        self.label_mensaje = QLabel('Mensaje de reclamo:')
        self.input_mensaje = QTextEdit()
        self.layout.addWidget(self.label_mensaje)
        self.layout.addWidget(self.input_mensaje)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.guardar_reclamo)
        button_box.rejected.connect(self.close)
        self.layout.addWidget(button_box)

    def guardar_reclamo(self):
        materia = self.input_materia.text().strip()
        mensaje = self.input_mensaje.toPlainText().strip()
        self.accept()  # Cerrar la ventana de reclamo
        # Llamar a la función para procesar el reclamo utilizando el estudiante guardado
        op.reclamar_nota(self.estudiante, materia, mensaje)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.maestro = None  # Inicializar maestro como None al principio
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Notas')
        self.setGeometry(400, 400, 800, 600)

        self.layout = QVBoxLayout(self)

        self.label_rol = QLabel('Ingrese su rol (maestro/estudiante):')
        self.input_rol = QLineEdit()
        self.layout.addWidget(self.label_rol)
        self.layout.addWidget(self.input_rol)

        self.label_nombre = QLabel('Ingrese su nombre:')
        self.input_nombre = QLineEdit()
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)

        self.btn_ingresar = QPushButton('Ingresar')
        self.btn_ingresar.clicked.connect(self.ingresar)
        self.layout.addWidget(self.btn_ingresar)

    def ingresar(self):
        rol = self.input_rol.text().strip().lower()
        nombre = self.input_nombre.text().strip()

        if rol == 'maestro':
            self.maestro = {'nombre': 'Profe Carlos', 'estudiantes': [
                {'nombre': "Juan", 'notas': {"Matemáticas": 90, "Historia": 85}},
                {'nombre': "María", 'notas': {"Matemáticas": 78, "Historia": 92}}
            ]}
            if nombre == self.maestro['nombre']:
                self.mostrar_menu_maestro(self.maestro)
            else:
                self.mostrar_mensaje('Nombre de maestro incorrecto')
        elif rol == 'estudiante':
            if self.maestro is not None:
                estudiante = op.buscar_estudiante(self.maestro, nombre)
                if estudiante:
                    self.mostrar_menu_estudiante(estudiante)
                else:
                    self.mostrar_mensaje('Nombre de estudiante incorrecto')
            else:
                self.mostrar_mensaje('Primero ingrese como maestro para continuar')
        else:
            self.mostrar_mensaje('Rol no válido')

    def mostrar_menu_maestro(self, maestro):
        self.limpiar_layout()

        self.label_opciones = QLabel('Opciones:')
        self.layout.addWidget(self.label_opciones)

        self.btn_ver_notas = QPushButton('Ver notas de estudiantes')
        self.btn_ver_notas.clicked.connect(lambda: self.mostrar_resultado(op.ver_notas_estudiantes(maestro)))
        self.layout.addWidget(self.btn_ver_notas)

        self.btn_cambiar_nota = QPushButton('Cambiar nota de estudiante')
        self.btn_cambiar_nota.clicked.connect(self.cambiar_nota)
        self.layout.addWidget(self.btn_cambiar_nota)

        self.btn_cargar_notas = QPushButton('Cargar notas desde archivo')
        self.btn_cargar_notas.clicked.connect(self.cargar_notas)
        self.layout.addWidget(self.btn_cargar_notas)

        self.btn_ver_reclamos = QPushButton('Ver reclamos de estudiantes')
        self.btn_ver_reclamos.clicked.connect(lambda: self.mostrar_resultado(op.ver_reclamos(maestro)))
        self.layout.addWidget(self.btn_ver_reclamos)

        self.btn_agregar_estudiante = QPushButton('Agregar estudiante')
        self.btn_agregar_estudiante.clicked.connect(self.agregar_estudiante)
        self.layout.addWidget(self.btn_agregar_estudiante)

        self.btn_quitar_estudiante = QPushButton('Quitar estudiante')
        self.btn_quitar_estudiante.clicked.connect(self.quitar_estudiante)
        self.layout.addWidget(self.btn_quitar_estudiante)

        self.btn_salir = QPushButton('Salir')
        self.btn_salir.clicked.connect(self.volver_inicio)
        self.layout.addWidget(self.btn_salir)

    def mostrar_menu_estudiante(self, estudiante):
        self.limpiar_layout()

        self.label_opciones = QLabel('Opciones:')
        self.layout.addWidget(self.label_opciones)

        self.btn_ver_notas = QPushButton('Ver mis notas')
        self.btn_ver_notas.clicked.connect(lambda: self.mostrar_resultado(op.ver_notas(estudiante)))
        self.layout.addWidget(self.btn_ver_notas)

        self.btn_reclamar_nota = QPushButton('Reclamar nota')
        self.btn_reclamar_nota.clicked.connect(lambda: self.abrir_ventana_reclamo(estudiante))
        self.layout.addWidget(self.btn_reclamar_nota)

        self.btn_salir = QPushButton('Salir')
        self.btn_salir.clicked.connect(self.volver_inicio)
        self.layout.addWidget(self.btn_salir)

    def abrir_ventana_reclamo(self, estudiante):
        ventana_reclamo = VentanaReclamo(estudiante, self)
        if ventana_reclamo.exec_():
            # Si el reclamo se guarda correctamente, puedes realizar alguna acción adicional si lo necesitas
            pass

    def cambiar_nota(self):
        if self.maestro is not None:
            nombre_estudiante, ok = QInputDialog.getText(self, 'Cambiar nota', 'Nombre del estudiante:')
            if ok and nombre_estudiante:
                materia, ok = QInputDialog.getText(self, 'Cambiar nota', 'Materia:')
                if ok and materia:
                    nueva_nota, ok = QInputDialog.getText(self, 'Cambiar nota', 'Nueva nota:')
                    if ok and nueva_nota:
                        op.cambiar_nota(self.maestro, nombre_estudiante, materia, nueva_nota)
                        self.mostrar_mensaje(f'Nota cambiada para {nombre_estudiante} en {materia}')
        else:
            self.mostrar_mensaje('Primero ingrese como maestro para cambiar notas')

    def cargar_notas(self):
        if self.maestro is not None:
            archivo, ok = QInputDialog.getText(self, 'Cargar notas', 'Ruta del archivo Excel:')
            if ok and archivo:
                op.cargar_notas(self.maestro, archivo)
                self.mostrar_mensaje(f'Notas cargadas desde {archivo}')
        else:
            self.mostrar_mensaje('Primero ingrese como maestro para cargar notas')

    def agregar_estudiante(self):
        if self.maestro is not None:
            nombre_estudiante, ok = QInputDialog.getText(self, 'Agregar estudiante', 'Nombre del nuevo estudiante:')
            if ok and nombre_estudiante:
                op.agregar_estudiante(self.maestro, nombre_estudiante)
                self.mostrar_mensaje(f'Estudiante {nombre_estudiante} agregado')
        else:
            self.mostrar_mensaje('Primero ingrese como maestro para agregar estudiantes')

    def quitar_estudiante(self):
        if self.maestro is not None:
            nombre_estudiante, ok = QInputDialog.getText(self, 'Quitar estudiante', 'Nombre del estudiante a eliminar:')
            if ok and nombre_estudiante:
                op.quitar_estudiante(self.maestro, nombre_estudiante)
                self.mostrar_mensaje(f'Estudiante {nombre_estudiante} eliminado')
        else:
            self.mostrar_mensaje('Primero ingrese como maestro para quitar estudiantes')

    def limpiar_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def mostrar_resultado(self, resultado):
        self.layout.addWidget(QTextEdit(str(resultado)))

    def mostrar_mensaje(self, mensaje):
        self.limpiar_layout()
        self.layout.addWidget(QLabel(mensaje))

    def volver_inicio(self):
        self.limpiar_layout()
        self.initUI()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
