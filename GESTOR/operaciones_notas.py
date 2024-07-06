def buscar_estudiante(maestro, nombre_estudiante):
    for estudiante in maestro['estudiantes']:
        if estudiante['nombre'] == nombre_estudiante:
            return estudiante
    return None

def agregar_estudiante(maestro, nombre):
    nuevo_estudiante = {"nombre": nombre, "notas": {}}
    maestro['estudiantes'].append(nuevo_estudiante)

def cambiar_nota(maestro, nombre_estudiante, materia, nueva_nota):
    estudiante = buscar_estudiante(maestro, nombre_estudiante)
    if estudiante:
        estudiante['notas'][materia] = nueva_nota

def ver_notas(estudiante):
    return estudiante['notas']

def reclamar_nota(estudiante, materia, mensaje):
    # Esta función puede agregar el reclamo a una lista en el estudiante
    # o enviarlo de alguna manera al maestro.
    # Aquí solo se muestra un mensaje de éxito.
    return f"Reclamo enviado para {materia}: {mensaje}"

def ver_reclamos(maestro):
    # Esta función debería devolver una lista de reclamos.
    # Aquí se devuelve una lista de ejemplo.
    return ["Reclamo de Juan en Matemáticas: Quiero revisión de nota", 
            "Reclamo de María en Historia: No estoy de acuerdo con mi nota"]

def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas.values()) / len(notas)
