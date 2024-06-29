import operaciones_notas as op

def menu_maestro(maestro):
    """Muestra las opciones disponibles para el maestro y ejecuta la seleccionada."""
    while True:
        print("Opciones:\n1. Ver notas de estudiantes\n2. Cambiar nota de estudiante\n3. Cargar notas desde archivo\n4. Ver reclamos de estudiantes\n5. Agregar estudiante\n6. Quitar estudiante\n7. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print(op.ver_notas_estudiantes(maestro))
        elif opcion == "2":
            nombre_estudiante = input("Nombre del estudiante: ").strip()
            materia = input("Materia: ").strip()
            nueva_nota = float(input("Nueva nota: ").strip())
            op.cambiar_nota(maestro, nombre_estudiante, materia, nueva_nota)
        elif opcion == "3":
            archivo = input("Ruta del archivo Excel: ").strip()
            op.cargar_notas(maestro, archivo)
        elif opcion == "4":
            reclamos = op.ver_reclamos(maestro)
            if reclamos:
                for reclamo in reclamos:
                    print(reclamo)
            else:
                print("No hay reclamos registrados.")
        elif opcion == "5":
            nombre_estudiante = input("Nombre del nuevo estudiante: ").strip()
            op.agregar_estudiante(maestro, nombre_estudiante)
        elif opcion == "6":
            nombre_estudiante = input("Nombre del estudiante a eliminar: ").strip()
            op.quitar_estudiante(maestro, nombre_estudiante)
        elif opcion == "7":
            break
        else:
            print("Opción no válida")

def menu_estudiante(estudiante):
    """Muestra las opciones disponibles para el estudiante y ejecuta la seleccionada."""
    while True:
        print("Opciones:\n1. Ver mis notas\n2. Reclamar nota\n3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print(op.ver_notas(estudiante))
        elif opcion == "2":
            materia = input("Materia: ").strip()
            mensaje = input("Mensaje de reclamo: ").strip()
            print(op.reclamar_nota(estudiante, materia, mensaje))
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

def main():
    """Función principal que gestiona el flujo del programa."""
    estudiantes = [
        {'nombre': "Juan", 'notas': {"Matemáticas": 90, "Historia": 85}},
        {'nombre': "María", 'notas': {"Matemáticas": 78, "Historia": 92}}
    ]
    
    maestro = {'nombre': "Profe Carlos", 'estudiantes': estudiantes}
    
    while True:
        print("\nSistema de gestión de notas")
        rol = input("Ingrese su rol (maestro/estudiante): ").strip().lower()
        
        if rol == "maestro":
            nombre = input("Ingrese su nombre: ").strip()
            if nombre == maestro['nombre']:
                menu_maestro(maestro)
            else:
                print("Nombre de maestro incorrecto")
        
        elif rol == "estudiante":
            nombre = input("Ingrese su nombre: ").strip()
            estudiante = op.buscar_estudiante(maestro, nombre)
            if estudiante:
                menu_estudiante(estudiante)
            else:
                print("Nombre de estudiante incorrecto")
        else:
            print("Rol no válido")

if __name__ == "__main__":
    main()
