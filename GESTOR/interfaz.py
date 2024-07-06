import tkinter as tk
from tkinter import messagebox
import operaciones_notas as op

class Interfaz:
    def __init__(self, maestro):
        self.maestro = maestro
        self.estudiante = None
        self.root = tk.Tk()
        self.root.title('Gestión de Notas')
        self.root.geometry('600x400')
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.clear_widgets()

        self.label_titulo = tk.Label(self.root, text='GESTION DE NOTAS', font=('Helvetica', 20, 'bold'))
        self.label_titulo.pack(pady=10)

        self.label_usuario = tk.Label(self.root, text='USUARIO', font=('Helvetica', 16))
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(self.root, font=('Helvetica', 14))
        self.entry_usuario.pack(pady=5)

        self.btn_ok = tk.Button(self.root, text='OK', font=('Helvetica', 14), command=self.ok)
        self.btn_ok.pack(pady=5)

        self.label_rol = tk.Label(self.root, text='ROL', font=('Helvetica', 16))
        self.label_rol.pack(pady=10)

        self.rol_var = tk.StringVar(value='MAESTRO')
        self.radio_maestro = tk.Radiobutton(self.root, text='MAESTRO', variable=self.rol_var, value='MAESTRO', font=('Helvetica', 14))
        self.radio_maestro.pack(anchor=tk.W)

        self.radio_estudiante = tk.Radiobutton(self.root, text='ESTUDIANTE', variable=self.rol_var, value='ESTUDIANTE', font=('Helvetica', 14))
        self.radio_estudiante.pack(anchor=tk.W)

        # Botón para regresar al menú principal
        self.btn_regresar = tk.Button(self.root, text='Regresar al Menú Principal', font=('Helvetica', 14), command=self.mostrar_menu_principal)
        self.btn_regresar.pack(pady=5)
        self.btn_regresar.pack_forget()  # Inicialmente oculto

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def ok(self):
        user = self.entry_usuario.get()
        role = self.rol_var.get()

        if role == 'MAESTRO':
            if user == self.maestro['nombre']:
                self.mostrar_menu_maestro()
            else:
                messagebox.showerror("Error", "Nombre de maestro incorrecto")
        else:
            estudiante = op.buscar_estudiante(self.maestro, user)
            if estudiante:
                self.estudiante = estudiante
                self.mostrar_menu_estudiante()
            else:
                messagebox.showerror("Error", "Nombre de estudiante incorrecto")

    def mostrar_menu_principal(self):
        self.clear_widgets()

        self.label_titulo = tk.Label(self.root, text='GESTION DE NOTAS', font=('Helvetica', 20, 'bold'))
        self.label_titulo.pack(pady=10)

        self.label_usuario = tk.Label(self.root, text='USUARIO', font=('Helvetica', 16))
        self.label_usuario.pack()

        self.entry_usuario = tk.Entry(self.root, font=('Helvetica', 14))
        self.entry_usuario.pack(pady=5)

        self.btn_ok = tk.Button(self.root, text='OK', font=('Helvetica', 14), command=self.ok)
        self.btn_ok.pack(pady=5)

        self.label_rol = tk.Label(self.root, text='ROL', font=('Helvetica', 16))
        self.label_rol.pack(pady=10)

        self.rol_var = tk.StringVar(value='MAESTRO')
        self.radio_maestro = tk.Radiobutton(self.root, text='MAESTRO', variable=self.rol_var, value='MAESTRO', font=('Helvetica', 14))
        self.radio_maestro.pack(anchor=tk.W)

        self.radio_estudiante = tk.Radiobutton(self.root, text='ESTUDIANTE', variable=self.rol_var, value='ESTUDIANTE', font=('Helvetica', 14))
        self.radio_estudiante.pack(anchor=tk.W)

        # Mostramos el botón de regresar al menú principal
        self.btn_regresar.pack(pady=5)

    def mostrar_menu_maestro(self):
        self.clear_widgets()

        self.label_aniadir_estudiantes = tk.Label(self.root, text='Añadir Estudiantes', font=('Helvetica', 14))
        self.label_aniadir_estudiantes.pack(pady=5)

        self.frame_estudiantes = tk.Frame(self.root)
        self.frame_estudiantes.pack(pady=5)

        tk.Label(self.frame_estudiantes, text='Nombre', font=('Helvetica', 12)).grid(row=0, column=0, padx=10)
        self.entry_nombre_estudiante = tk.Entry(self.frame_estudiantes, font=('Helvetica', 12))
        self.entry_nombre_estudiante.grid(row=1, column=0, padx=10, pady=2)

        self.btn_agregar_estudiante = tk.Button(self.frame_estudiantes, text='Agregar Estudiante', font=('Helvetica', 12), command=self.agregar_estudiante)
        self.btn_agregar_estudiante.grid(row=1, column=1, padx=10, pady=2)

        self.label_cambiar_notas = tk.Label(self.root, text='Cambiar Notas', font=('Helvetica', 14))
        self.label_cambiar_notas.pack(pady=5)

        self.frame_notas = tk.Frame(self.root)
        self.frame_notas.pack(pady=5)

        tk.Label(self.frame_notas, text='Nombre', font=('Helvetica', 12)).grid(row=0, column=0, padx=10)
        self.entry_nombre_nota = tk.Entry(self.frame_notas, font=('Helvetica', 12))
        self.entry_nombre_nota.grid(row=1, column=0, padx=10, pady=2)

        tk.Label(self.frame_notas, text='Materia', font=('Helvetica', 12)).grid(row=0, column=1, padx=10)
        self.entry_materia_nota = tk.Entry(self.frame_notas, font=('Helvetica', 12))
        self.entry_materia_nota.grid(row=1, column=1, padx=10, pady=2)

        tk.Label(self.frame_notas, text='Nota', font=('Helvetica', 12)).grid(row=0, column=2, padx=10)
        self.entry_nueva_nota = tk.Entry(self.frame_notas, font=('Helvetica', 12))
        self.entry_nueva_nota.grid(row=1, column=2, padx=10, pady=2)

        self.btn_cambiar_nota = tk.Button(self.frame_notas, text='Cambiar Nota', font=('Helvetica', 12), command=self.cambiar_nota)
        self.btn_cambiar_nota.grid(row=1, column=3, padx=10, pady=2)

        self.label_reclamos = tk.Label(self.root, text='Reclamos', font=('Helvetica', 14))
        self.label_reclamos.pack(pady=5)

        self.frame_reclamos = tk.Frame(self.root)
        self.frame_reclamos.pack(pady=5)

        self.btn_ver_reclamos = tk.Button(self.frame_reclamos, text='Ver Reclamos', font=('Helvetica', 12), command=self.ver_reclamos)
        self.btn_ver_reclamos.pack()

        # Botón para actualizar notas
        self.btn_actualizar_notas = tk.Button(self.root, text='Actualizar Notas', font=('Helvetica', 12), command=self.actualizar_notas)
        self.btn_actualizar_notas.pack(pady=5)

        # Mostramos el botón de regresar al menú principal
        self.btn_regresar.pack(pady=5)

    def agregar_estudiante(self):
        nombre_estudiante = self.entry_nombre_estudiante.get()
        op.agregar_estudiante(self.maestro, nombre_estudiante)
        messagebox.showinfo("Éxito", f"Estudiante '{nombre_estudiante}' agregado correctamente")

    def cambiar_nota(self):
        nombre_estudiante = self.entry_nombre_nota.get()
        materia = self.entry_materia_nota.get()
        nueva_nota = float(self.entry_nueva_nota.get())
        op.cambiar_nota(self.maestro, nombre_estudiante, materia, nueva_nota)
        messagebox.showinfo("Éxito", f"Nota de '{materia}' cambiada correctamente para '{nombre_estudiante}'")

    def ver_reclamos(self):
        reclamos = op.ver_reclamos(self.maestro)
        messagebox.showinfo("Reclamos", "\n".join(reclamos))

    def actualizar_notas(self):
        # Esta función podría incluir lógica adicional para actualizar las notas en la interfaz.
        messagebox.showinfo("Éxito", "Notas actualizadas correctamente")

    def mostrar_menu_estudiante(self):
        self.clear_widgets()

        self.label_bienvenida_estudiante = tk.Label(self.root, text=f'Bienvenido, {self.estudiante["nombre"]}', font=('Helvetica', 16))
        self.label_bienvenida_estudiante.pack(pady=10)

        self.label_ver_notas = tk.Label(self.root, text='Ver Notas', font=('Helvetica', 14))
        self.label_ver_notas.pack(pady=5)

        self.btn_ver_notas = tk.Button(self.root, text='Ver Notas', font=('Helvetica', 12), command=self.ver_notas_estudiante)
        self.btn_ver_notas.pack(pady=5)

        self.label_reclamar_nota = tk.Label(self.root, text='Reclamar Nota', font=('Helvetica', 14))
        self.label_reclamar_nota.pack(pady=5)

        self.frame_reclamar_nota = tk.Frame(self.root)
        self.frame_reclamar_nota.pack(pady=5)

        tk.Label(self.frame_reclamar_nota, text='Materia', font=('Helvetica', 12)).grid(row=0, column=0, padx=10)
        self.entry_materia_reclamo = tk.Entry(self.frame_reclamar_nota, font=('Helvetica', 12))
        self.entry_materia_reclamo.grid(row=0, column=1, padx=10, pady=2)

        tk.Label(self.frame_reclamar_nota, text='Mensaje', font=('Helvetica', 12)).grid(row=1, column=0, padx=10)
        self.entry_mensaje_reclamo = tk.Entry(self.frame_reclamar_nota, font=('Helvetica', 12))
        self.entry_mensaje_reclamo.grid(row=1, column=1, padx=10, pady=2)

        self.btn_reclamar_nota = tk.Button(self.frame_reclamar_nota, text='Reclamar Nota', font=('Helvetica', 12), command=self.reclamar_nota)
        self.btn_reclamar_nota.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Mostramos el botón de regresar al menú principal
        self.btn_regresar.pack(pady=5)

    def ver_notas_estudiante(self):
        notas = op.ver_notas(self.estudiante)
        messagebox.showinfo(f'Notas de {self.estudiante["nombre"]}', "\n".join(f'{materia}: {nota}' for materia, nota in notas.items()))

    def reclamar_nota(self):
        materia = self.entry_materia_reclamo.get()
        mensaje = self.entry_mensaje_reclamo.get()
        mensaje_enviado = op.reclamar_nota(self.estudiante, materia, mensaje)
        messagebox.showinfo("Éxito", mensaje_enviado)

if __name__ == '__main__':
    # Ejemplo de múltiples profesores
    profesores = [
    {
        "nombre": "Prof. Carlos",
        "estudiantes": [
            {"nombre": "Juan", "notas": {"Matemáticas": 5.0, "Historia": 4.5}},
            {"nombre": "María", "notas": {"Matemáticas": 4.0, "Historia": 3.5}},
        ]
    },
    {
        "nombre": "Prof. Miguel",
        "estudiantes": [
            {"nombre": "Luis", "notas": {"Matemáticas": 3.5, "Historia": 4.0}},
            {"nombre": "Ana", "notas": {"Matemáticas": 4.5, "Historia": 5.0}},
        ]
    },
    {
        "nombre": "Prof. Mario",
        "estudiantes": [
            {"nombre": "Carlos", "notas": {"Matemáticas": 4.0, "Historia": 3.0}},
            {"nombre": "Lucía", "notas": {"Matemáticas": 5.0, "Historia": 4.5}},
        ]
    },
    {
        "nombre": "Prof. Andrés",
        "estudiantes": [
            {"nombre": "Pedro", "notas": {"Matemáticas": 2.5, "Historia": 3.5}},
            {"nombre": "Sofía", "notas": {"Matemáticas": 4.5, "Historia": 4.0}},
        ]
    },
    {
        "nombre": "Prof. Mariana",
        "estudiantes": [
            {"nombre": "Raúl", "notas": {"Matemáticas": 3.0, "Historia": 3.5}},
            {"nombre": "Diana", "notas": {"Matemáticas": 4.0, "Historia": 4.5}},
        ]
    },
    {
        "nombre": "Prof. Isabela",
        "estudiantes": [
            {"nombre": "Hugo", "notas": {"Matemáticas": 5.0, "Historia": 5.0}},
            {"nombre": "Valeria", "notas": {"Matemáticas": 4.0, "Historia": 3.5}},
        ]
    },
    {
        "nombre": "Prof. Daniela",
        "estudiantes": [
            {"nombre": "Javier", "notas": {"Matemáticas": 3.5, "Historia": 4.0}},
            {"nombre": "Martina", "notas": {"Matemáticas": 4.5, "Historia": 4.5}},
        ]
    },
    {
        "nombre": "Prof. Luisa",
        "estudiantes": [
            {"nombre": "Fernando", "notas": {"Matemáticas": 4.0, "Historia": 4.0}},
            {"nombre": "Camila", "notas": {"Matemáticas": 3.0, "Historia": 3.5}},
        ]
    }
]

    # Ejemplo: Inicializar la interfaz con el primer profesor de la lista
    interfaz_principal = Interfaz(profesores[0])
