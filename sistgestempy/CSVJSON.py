import csv
import json

# Función para añadir una pizza al fichero CSV
def guardar_pizza_csv(pizza, fichero='pizzas.csv'):
    try:
        # Abrir el fichero CSV (en modo) append para añadir una nueva pizza
        with open(fichero, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Guardar la pizza: tamaño y lista de ingredientes (convertida a cadena)
            writer.writerow([pizza['tamaño'], ', '.join(pizza['ingredientes'])])
        print("Pizza guardada en el archivo CSV.")
    except Exception as e:
        print(f"Error al guardar la pizza en el archivo CSV: {e}")

# Función para añadir una pizza al fichero JSON
def guardar_pizza_json(pizza, fichero='pizzas.json'):
    try:
        pizzas = []
        # Leer el archivo JSON para cargar las pizzas existentes
        try:
            with open(fichero, 'r', encoding='utf-8') as file:
                pizzas = json.load(file)
        except FileNotFoundError:
            pass  # Si el archivo no existe, crea uno
        
        # Añadir la nueva pizza a la lista
        pizzas.append(pizza)
        
        # Guardar la lista completa de pizzas en el archivo JSON
        with open(fichero, 'w', encoding='utf-8') as file:
            json.dump(pizzas, file, indent=4, ensure_ascii=False)
        print("Pizza guardada en el archivo JSON.")
    except Exception as e:
        print(f"Error al guardar la pizza en el archivo JSON: {e}")

def pedir_pizza():
    tamaño = input("Introduce el tamaño de la pizza (mediana/grande): ").lower()
    while tamaño not in ['mediana', 'grande']:
        print("Tamaño no válido. Debe ser 'mediana' o 'grande'.")
        tamaño = input("Introduce el tamaño de la pizza (mediana/grande): ").lower()

    ingredientes = []
    while True:
        ingrediente = input("Introduce un ingrediente (o 'fin' para terminar): ")
        if ingrediente.lower() == 'fin':
            break
        ingredientes.append(ingrediente)
        
    pizza = {
        'tamaño': tamaño,
        'ingredientes': ingredientes
    }
    return pizza

def menu():
    while True:
        print("\nMenú de Gestión de Pizzas")
        print("1. Añadir una pizza")
        print("2. Salir")
        
        opcion = input("Selecciona una opción (1-2): ")

        if opcion == "1":
            pizza = pedir_pizza()
            guardar_pizza_csv(pizza)
            guardar_pizza_json(pizza)
        elif opcion == "2":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor selecciona una opción entre 1 y 2.")

# Ejecuta el programa
menu()
