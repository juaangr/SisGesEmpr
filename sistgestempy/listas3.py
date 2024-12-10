import datetime

# Lista para los usrs
usuarios = []

def añadir_usuario():
    id_usuario = input("Introduce el ID del usuario: ")
    fecha_creacion = input("Introduce la fecha de creación del usuario (dd-mm-yyyy): ")
    rol = input("Introduce el rol del usuario (usuario, usuario avanzado, admin): ").lower()

    if rol not in ["usuario", "usuario avanzado", "admin"]:
        print("Rol no válido. Los roles permitidos son: usuario, usuario avanzado, admin.")
        return

    try:
        fecha = [int(i) for i in fecha_creacion.split('-')]
        if len(fecha) != 3:
            raise ValueError
        fecha_creacion = fecha
    except ValueError:
        print("Formato de fecha incorrecto. Debe ser dd-mm-yyyy.")
        return
    
    usuarios.append([id_usuario, fecha_creacion, rol])
    print(f"Usuario {id_usuario} añadido con éxito.")
    
def mostrar_usuarios():
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Fecha de Creación: {usuario[1]}, Rol: {usuario[2]}")

def modificar_usuario():
    id_usuario = input("Introduce el ID del usuario que deseas modificar: ")

    for usuario in usuarios:
        if usuario[0] == id_usuario:
            print(f"Usuario encontrado: ID: {usuario[0]}, Fecha: {usuario[1]}, Rol: {usuario[2]}")
            campo = input("¿Qué deseas modificar? (fecha/rol): ").lower()
            if campo == "fecha":
                nueva_fecha = input("Introduce la nueva fecha de creación (dd-mm-yyyy): ")
                try:
                    nueva_fecha = [int(i) for i in nueva_fecha.split('-')]
                    if len(nueva_fecha) != 3:
                        raise ValueError
                    usuario[1] = nueva_fecha
                    print(f"Fecha de creación actualizada a: {usuario[1]}")
                except ValueError:
                    print("Formato de fecha incorrecto. Debe ser dd-mm-yyyy.")
            elif campo == "rol":
                nuevo_rol = input("Introduce el nuevo rol (usuario, usuario avanzado, admin): ").lower()
                if nuevo_rol in ["usuario", "usuario avanzado", "admin"]:
                    usuario[2] = nuevo_rol
                    print(f"Rol actualizado a: {usuario[2]}")
                else:
                    print("Rol no válido.")
            else:
                print("Opción no válida.")
            return
        
    print(f"No se encontró un usuario con ID {id_usuario}.")

def borrar_usuario():
    id_usuario = input("Introduce el ID del usuario que deseas borrar: ")
    
    for usuario in usuarios:
        if usuario[0] == id_usuario:
            usuarios.remove(usuario)
            print(f"Usuario {id_usuario} borrado con éxito.")
            return
    
    print(f"No se encontró un usuario con ID {id_usuario}.")

def mostrar_fechas():
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"Fecha de Creación: {usuario[1]}")

def menu():
    while True:
        print("\nMenú de Gestión de Usuarios")
        print("1. Añadir usuario")
        print("2. Mostrar usuarios")
        print("3. Modificar usuario")
        print("4. Borrar usuario")
        print("5. Mostrar fechas")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            añadir_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            borrar_usuario()
        elif opcion == "5":
            mostrar_fechas()
        elif opcion == "6":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 6.")

#Para ejecutar el programa
menu()
