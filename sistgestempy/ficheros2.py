def mostrar_cabecera(fichero, num_lineas):
    try:
        with open(fichero, 'r') as f:
            lineas = f.readlines()
            for i in range(min(num_lineas, len(lineas))):
                print(lineas[i].strip())
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print(f"Error al leer el fichero: {e}")

def mostrar_pie(fichero, num_lineas):
    try:
        with open(fichero, 'r') as f:
            lineas = f.readlines()
            for i in range(max(0, len(lineas) - num_lineas), len(lineas)):
                print(lineas[i].strip())
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print(f"Error al leer el fichero: {e}")

def añadir_lineas(fichero):
    try:
        with open(fichero, 'a') as f:
            for i in range(10):
                numero = input(f"Introduce el número {i+1}: ")
                f.write(f"Línea con el número {numero}\n")
            print("10 líneas añadidas con éxito.")
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print(f"Error al escribir en el fichero: {e}")

def borrar_lineas(fichero, num_lineas):
    try:
        with open(fichero, 'r') as f:
            lineas = f.readlines()

        if num_lineas >= len(lineas):
            print("El número de líneas a borrar es mayor o igual al número total de líneas en el fichero.")
            return
        
        lineas = lineas[num_lineas:]

        with open(fichero, 'w') as f:
            f.writelines(lineas)
        print(f"{num_lineas} líneas borradas del principio del fichero.")
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print(f"Error al procesar el fichero: {e}")

def menu():
    fichero = 'fichero.txt'
    
    while True:
        print("\nMenú de Opciones:")
        print("1. Mostrar cabecera")
        print("2. Mostrar pie")
        print("3. Añadir líneas")
        print("4. Borrar líneas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            num_lineas = int(input("¿Cuántas líneas deseas mostrar desde el principio? "))
            mostrar_cabecera(fichero, num_lineas)
        elif opcion == "2":
            num_lineas = int(input("¿Cuántas líneas deseas mostrar desde el final? "))
            mostrar_pie(fichero, num_lineas)
        elif opcion == "3":
            añadir_lineas(fichero)
        elif opcion == "4":
            num_lineas = int(input("¿Cuántas líneas deseas borrar desde el principio? "))
            borrar_lineas(fichero, num_lineas)
        elif opcion == "5":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 5.")

# Ejecuta el programa
menu()
