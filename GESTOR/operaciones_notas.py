import pandas as pd

def cargar_notas(maestro, archivo_excel):
    """Carga las notas de los estudiantes desde un archivo Excel usando Pandas."""
    try:
        # Eliminar comillas dobles adicionales si están presentes
        archivo_excel = archivo_excel.strip('"')
        df = pd.read_excel(archivo_excel)
        for i, row in df.iterrows():
            nombre_estudiante = row['Nombre']
            estudiante = buscar_estudiante(maestro, nombre_estudiante)
            if estudiante:
                for col in df.columns:
                    if col != 'Nombre':
                        estudiante['notas'][col] = row[col]
            else:
                nuevo_estudiante = {'nombre': nombre_estudiante, 'notas': {col: row[col] for col in df.columns if col != 'Nombre'}}
                maestro['estudiantes'].append(nuevo_estudiante)
    except Exception as e:
        print(f"Error al cargar las notas: {e}")

def ver_notas_estudiantes(maestro):
    """Devuelve las notas de todos los estudiantes."""
    return {est['nombre']: est['notas'] for est in maestro['estudiantes']}

def cambiar_nota(maestro, nombre_estudiante, materia, nueva_nota):
    """Cambia la nota de un estudiante en una materia específica."""
    estudiante = buscar_estudiante(maestro, nombre_estudiante)
    if estudiante:
        estudiante['notas'][materia] = nueva_nota
    else:
        print(f"Estudiante {nombre_estudiante} no encontrado")

def ver_reclamos(maestro):
    """Devuelve los reclamos de todos los estudiantes."""
    reclamos = []
    for estudiante in maestro['estudiantes']:
        if 'reclamos' in estudiante:
            for materia, reclamo in estudiante['reclamos'].items():
                reclamos.append(f"Estudiante: {estudiante['nombre']}, Materia: {materia}, Reclamo: {reclamo}")
    return reclamos

def agregar_estudiante(maestro, nombre_estudiante):
    """Agrega un nuevo estudiante al sistema."""
    nuevo_estudiante = {'nombre': nombre_estudiante, 'notas': {}}
    maestro['estudiantes'].append(nuevo_estudiante)
    print(f"Estudiante {nombre_estudiante} agregado exitosamente.")

def quitar_estudiante(maestro, nombre_estudiante):
    """Quita un estudiante del sistema."""
    estudiante = buscar_estudiante(maestro, nombre_estudiante)
    if estudiante:
        maestro['estudiantes'].remove(estudiante)
        print(f"Estudiante {nombre_estudiante} eliminado exitosamente.")
    else:
        print(f"Estudiante {nombre_estudiante} no encontrado.")

def buscar_estudiante(maestro, nombre_estudiante):
    """Busca un estudiante por nombre."""
    return next((est for est in maestro['estudiantes'] if est['nombre'] == nombre_estudiante), None)

def ver_notas(estudiante):
    """Devuelve las notas del estudiante."""
    return estudiante['notas']

def reclamar_nota(estudiante, materia, mensaje):
    """Simula el envío de un reclamo sobre una nota específica."""
    if 'reclamos' not in estudiante:
        estudiante['reclamos'] = {}
    estudiante['reclamos'][materia] = mensaje
    return f"Reclamo enviado por {estudiante['nombre']} sobre {materia}: {mensaje}"
