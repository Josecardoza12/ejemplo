#holaa
estudiantes = {}

def agregar_estudiantes(datos):
    rut = input("rut: ")
    if rut in datos:
        print("Este rut ya existe.")
    else:
        nombre = input("nombre: ")
        carrera = input("carrera: ")
        datos[rut] = {"rut":rut, "nombre":nombre,"carrera":carrera}
        print("Datos agregados.")

def modificar_estudiantes(datos):
    rut = input("Ingrese rut a modificar: ")
    if rut in datos:
        nuevo_nombre = input("Ingrese nuevo nombre: ")
        nueva_carrera = input("ingrese nueva carrera: ")

        if nuevo_nombre:
            datos[rut] ["nombre"] = nuevo_nombre
        if nueva_carrera:
            datos[rut] ["carrera"] = nueva_carrera
        if nuevo_nombre or nueva_carrera:
             print("datos modificados")
        else:
                print("no se realizaron cambios")
            
    else:
            print("El rut no existe")
def eliminar_estudiantes(datos):
    rut = input("Ingrese rut a eliminar: ")
    if rut in datos:
        del(datos[rut])
        print("Dato eliminado")
    else:
        print("El rut no existe")

def mostrar_estudiantes(datos):
    if not datos:
        print("No hay datos registrados")
    else:
        print("Estudiantes registrados: ")
        for rut,dato in datos.items():
            print(f"rut: {rut}")
            print(f"nombre: {dato['nombre']}")
            print(f"carrera: {dato['carrera']}")
            print("--------------------------")
def menu(datos):
    while True:
        print("Gestion de estudiantes.")
        print("1) Agregar estudiantes.")
        print("2) Modificar estudiantes")
        print("3) Eliminar estudiantes.")
        print("4) Mostrar estudiantes")
        print("5) Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            agregar_estudiantes(datos)
        elif opcion == 2:
            modificar_estudiantes(datos)
        elif opcion == 3:
            eliminar_estudiantes(datos)
        elif opcion == 4:
            mostrar_estudiantes(datos)
        elif opcion == 5:
            print("Hasta luego...")
            break
        else:
            print("opcion invalida")    
menu(estudiantes)


