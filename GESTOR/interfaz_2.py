import tkinter as tk
from tkinter import messagebox, simpledialog
import operaciones_notas as op

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Gestión de Notas')
        self.geometry('400x300')

        self.current_user = None  # Variable para almacenar el usuario actual (maestro o estudiante)
        self.previous_view = None  # Variable para almacenar la vista anterior

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
        self.previous_view = self.current_user
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

    def retroceder(self):
        if self.previous_view == 'maestro':
            self.current_user = 'maestro'
            self.mostrar_menu_maestro()
        elif self.previous_view == 'estudiante':
            self.current_user = self.previous_view
            self.mostrar_menu_estudiante()
        else:
            self.current_user = None
            self.create_widgets()

    def volver(self):
        self.label_usuario.config(text='USUARIO')
        self.retroceder()

    def mostrar_menu_maestro(self):
        self.clear_widgets()
        self.mostrar_opciones_comunes()

        self.btn_ver_notas = tk.Button(self, text='Ver notas de estudiantes', command=self.ver_notas_estudiantes)
        self.btn_ver_notas.pack()

        self.btn_cambiar_nota = tk.Button(self, text='Cambiar nota de estudiante', command=self.cambiar_nota_dialog)
        self.btn_cambiar_nota.pack()

        self.btn_cargar_notas = tk.Button(self, text='Cargar notas desde archivo', command=self.cargar_notas_dialog)
        self.btn_cargar_notas.pack()

        self.btn_ver_reclamos = tk.Button(self, text='Ver reclamos de estudiantes', command=self.ver_reclamos)
        self.btn_ver_reclamos.pack()

        self.btn_agregar_estudiante = tk.Button(self, text='Agregar estudiante', command=self.agregar_estudiante_dialog)
        self.btn_agregar_estudiante.pack()

        self.btn_quitar_estudiante = tk.Button(self, text='Quitar estudiante', command=self.quitar_estudiante_dialog)
        self.btn_quitar_estudiante.pack()

        self.btn_retroceder = tk.Button(self, text='Retroceder', command=self.retroceder)
        self.btn_retroceder.pack()

    def mostrar_menu_estudiante(self):
        self.clear_widgets()
        self.mostrar_opciones_comunes()

        self.btn_ver_notas = tk.Button(self, text='Ver mis notas', command=self.ver_notas_estudiante)
        self.btn_ver_notas.pack()

        self.btn_reclamar_nota = tk.Button(self, text='Reclamar nota', command=self.reclamar_nota_dialog)
        self.btn_reclamar_nota.pack()

        self.btn_retroceder = tk.Button(self, text='Retroceder', command=self.retroceder)
        self.btn_retroceder.pack()

    def mostrar_opciones_comunes(self):
        self.label_opciones = tk.Label(self, text='Opciones:')
        self.label_opciones.pack(pady=10)

    def ver_notas_estudiantes(self):
        self.mostrar_resultado(op.ver_notas_estudiantes(self.maestro))

    def ver_notas_estudiante(self):
        self.mostrar_resultado(op.ver_notas(self.current_user))

    def cambiar_nota_dialog(self):
        self.cambiar_nota_dialog_helper(self.maestro)

    def cambiar_nota_dialog_helper(self, maestro):
        nombre_estudiante = simpledialog.askstring('Cambiar Nota', 'Nombre del estudiante:')
        if not nombre_estudiante:
            return
        
        materia = simpledialog.askstring('Cambiar Nota', 'Materia:')
        if not materia:
            return
        
        nueva_nota = simpledialog.askstring('Cambiar Nota', 'Nueva nota:')
        if not nueva_nota:
            return
        
        op.cambiar_nota(maestro, nombre_estudiante, materia, nueva_nota)
        messagebox.showinfo('Cambiar Nota', 'Nota cambiada exitosamente.')
        self.retroceder()

    def cargar_notas_dialog(self):
        archivo = simpledialog.askstring('Cargar Notas', 'Ruta del archivo Excel:')
        if archivo:
            op.cargar_notas(self.maestro, archivo)
            messagebox.showinfo('Cargar Notas', 'Notas cargadas exitosamente.')
            self.retroceder()

    def agregar_estudiante_dialog(self):
        nombre_estudiante = simpledialog.askstring('Agregar Estudiante', 'Nombre del nuevo estudiante:')
        if nombre_estudiante:
            op.agregar_estudiante(self.maestro, nombre_estudiante)
            messagebox.showinfo('Agregar Estudiante', 'Estudiante agregado exitosamente.')
            self.retroceder()

    def quitar_estudiante_dialog(self):
        nombre_estudiante = simpledialog.askstring('Quitar Estudiante', 'Nombre del estudiante a eliminar:')
        if nombre_estudiante:
            op.quitar_estudiante(self.maestro, nombre_estudiante)
            messagebox.showinfo('Quitar Estudiante', 'Estudiante eliminado exitosamente.')
            self.retroceder()

    def reclamar_nota_dialog(self):
        materia = simpledialog.askstring('Reclamar Nota', 'Materia:')
        if not materia:
            return
        
        mensaje = simpledialog.askstring('Reclamar Nota', 'Mensaje de reclamo:')
        if not mensaje:
            return
        
        op.reclamar_nota(self.current_user, materia, mensaje)
        messagebox.showinfo('Reclamar Nota', 'Nota reclamada exitosamente.')
        self.retroceder()

    def mostrar_resultado(self, resultado):
        self.clear_widgets()
        text_area = tk.Text(self)
        text_area.insert(tk.END, str(resultado))
        text_area.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        self.btn_retroceder = tk.Button(self, text='Retroceder', command=self.retroceder)
        self.btn_retroceder.pack()

    def mostrar_mensaje(self, mensaje):
        self.clear_widgets()
        label_mensaje = tk.Label(self, text=mensaje)
        label_mensaje.pack(padx=20, pady=20)

        self.btn_retroceder = tk.Button(self, text='Retroceder', command=self.retroceder)
        self.btn_retroceder.pack()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
