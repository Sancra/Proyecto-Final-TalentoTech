import tkinter as tk
from tkinter import messagebox, simpledialog
import operaciones_notas as op

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Gestión de Notas')
        self.geometry('400x300')

        self.current_user = None  # Variable para almacenar el usuario actual (maestro o estudiante)

        # Definir al maestro Carlos con dos estudiantes
        self.maestro = {
            'nombre': 'Carlos', 
            'estudiantes': [
                {'nombre': "Juan", 'notas': {"Matemáticas": 90, "Historia": 85}},
                {'nombre': "María", 'notas': {"Matemáticas": 78, "Historia": 92}}
            ]
        }

        self.create_widgets()

    def create_widgets(self):
        self.clear_widgets()

        self.label_usuario = tk.Label(self, text='USUARIO', font=('Helvetica', 16, 'bold'))
        self.label_usuario.pack(pady=10)

        self.btn_avanzar = tk.Button(self, text='Avanzar', command=self.avanzar)
        self.btn_avanzar.pack(side=tk.RIGHT, padx=10, pady=10)

        self.btn_volver = tk.Button(self, text='Volver', command=self.volver)
        self.btn_volver.pack(side=tk.RIGHT, padx=10, pady=10)

    def avanzar(self):
        self.clear_widgets()
        nombre_usuario = simpledialog.askstring('Ingresar Nombre', 'Nombre:')
        if not nombre_usuario:
            return
        
        if nombre_usuario == self.maestro['nombre']:
            self.current_user = 'maestro'
            self.mostrar_menu_maestro()
        else:
            estudiante = op.buscar_estudiante(self.maestro, nombre_usuario)
            if estudiante:
                self.current_user = estudiante
                self.mostrar_menu_estudiante()
            else:
                self.mostrar_mensaje('Usuario no registrado')

    def volver(self):
        self.label_usuario.config(text='USUARIO')
        self.clear_widgets()
        self.create_widgets()

    def mostrar_menu_maestro(self):
        self.clear_widgets()

        self.label_opciones = tk.Label(self, text='Opciones:')
        self.label_opciones.pack(pady=10)

        self.btn_ver_notas = tk.Button(self, text='Ver notas de estudiantes', command=self.ver_notas_estudiantes)
        self.btn_ver_notas.pack()

        self.btn_cambiar_nota = tk.Button(self, text='Cambiar nota de estudiante', command=self.cambiar_nota)
        self.btn_cambiar_nota.pack()

        self.btn_cargar_notas = tk.Button(self, text='Cargar notas desde archivo', command=self.cargar_notas)
        self.btn_cargar_notas.pack()

        self.btn_ver_reclamos = tk.Button(self, text='Ver reclamos de estudiantes', command=self.ver_reclamos)
        self.btn_ver_reclamos.pack()

        self.btn_agregar_estudiante = tk.Button(self, text='Agregar estudiante', command=self.agregar_estudiante)
        self.btn_agregar_estudiante.pack()

        self.btn_quitar_estudiante = tk.Button(self, text='Quitar estudiante', command=self.quitar_estudiante)
        self.btn_quitar_estudiante.pack()

        self.btn_volver = tk.Button(self, text='Volver', command=self.volver)
        self.btn_volver.pack()

    def mostrar_menu_estudiante(self):
        self.clear_widgets()

        self.label_opciones = tk.Label(self, text='Opciones:')
        self.label_opciones.pack(pady=10)

        self.btn_ver_notas = tk.Button(self, text='Ver mis notas', command=self.ver_notas_estudiante)
        self.btn_ver_notas.pack()

        self.btn_reclamar_nota = tk.Button(self, text='Reclamar nota', command=self.reclamar_nota)
        self.btn_reclamar_nota.pack()

        self.btn_volver = tk.Button(self, text='Volver', command=self.volver)
        self.btn_volver.pack()

    def ver_notas_estudiantes(self):
        self.clear_widgets()
        resultado = op.ver_notas_estudiantes(self.maestro)
        self.mostrar_resultado(resultado)

    def ver_notas_estudiante(self):
        self.clear_widgets()
        resultado = op.ver_notas(self.current_user)
        self.mostrar_resultado(resultado)

    def cambiar_nota(self):
        nombre_estudiante = simpledialog.askstring('Cambiar Nota', 'Nombre del estudiante:')
        if nombre_estudiante:
            materia = simpledialog.askstring('Cambiar Nota', 'Materia:')
            if materia:
                nueva_nota = simpledialog.askstring('Cambiar Nota', 'Nueva nota:')
                if nueva_nota:
                    op.cambiar_nota(self.maestro, nombre_estudiante, materia, nueva_nota)
                    messagebox.showinfo('Cambiar Nota', 'Nota cambiada exitosamente.')
                    self.volver()

    def cargar_notas(self):
        archivo = simpledialog.askstring('Cargar Notas', 'Ruta del archivo Excel:')
        if archivo:
            op.cargar_notas(self.maestro, archivo)
            messagebox.showinfo('Cargar Notas', 'Notas cargadas exitosamente.')
            self.volver()

    def agregar_estudiante(self):
        nombre_estudiante = simpledialog.askstring('Agregar Estudiante', 'Nombre del nuevo estudiante:')
        if nombre_estudiante:
            op.agregar_estudiante(self.maestro, nombre_estudiante)
            messagebox.showinfo('Agregar Estudiante', 'Estudiante agregado exitosamente.')
            self.volver()

    def quitar_estudiante(self):
        nombre_estudiante = simpledialog.askstring('Quitar Estudiante', 'Nombre del estudiante a eliminar:')
        if nombre_estudiante:
            op.quitar_estudiante(self.maestro, nombre_estudiante)
            messagebox.showinfo('Quitar Estudiante', 'Estudiante eliminado exitosamente.')
            self.volver()

    def reclamar_nota(self):
        materia = simpledialog.askstring('Reclamar Nota', 'Materia:')
        if materia:
            mensaje = simpledialog.askstring('Reclamar Nota', 'Mensaje de reclamo:')
            if mensaje:
                op.reclamar_nota(self.current_user, materia, mensaje)
                messagebox.showinfo('Reclamar Nota', 'Nota reclamada exitosamente.')
                self.volver()

    def mostrar_resultado(self, resultado):
        self.clear_widgets()
        text_area = tk.Text(self)
        text_area.insert(tk.END, str(resultado))
        text_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.btn_volver = tk.Button(self, text='Volver', command=self.volver)
        self.btn_volver.pack()

    def mostrar_mensaje(self, mensaje):
        self.clear_widgets()
        label_mensaje = tk.Label(self, text=mensaje)
        label_mensaje.pack(padx=20, pady=20)

        self.btn_volver = tk.Button(self, text='Volver', command=self.volver)
        self.btn_volver.pack()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
