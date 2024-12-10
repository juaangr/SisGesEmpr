import xml.etree.ElementTree as ET
import os 

# las variables que vamos a usar:
foodxml = ET.Element("food")
namexml = ET.Element("name")
pricexml = ET.Element("price")
descriptionxml = ("description")
caloriesxml = ET.Element("calories")

# con esto inicializamos nuestro arbol y el root del xml
def cargarMenu():
    tree = ET.parse("menuDesayuno.xml")
    root = tree.getroot()
    return root

def menuPrincipal():
    # menu del programa
    print("\n--- Menú Principal ---")
    print("1. Añadir plato")
    print("2. Modificar precio")
    print("3. Plato mas caro")
    print("4. Calcular Precio")
    print("5. Buscar Precio")
    print("6. Salir")
    while True:
        opcion = input("Elige una opción: ")
        if opcion == "1":
            ()
        elif opcion == "2":
            ()
        elif opcion == "3":
            ()
        elif opcion == "4":
            ()
        elif opcion == "5":
            ()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

def aniadirPlato(nuevo_plato):
    root, tree = cargarMenu()
    # permite introducir un nuevo plato al archivo
    print("Introduce los campos separados por comas")
    input(namexml, pricexml, descriptionxml, caloriesxml) #lista
    # verifica que no haya un plato igual
    for namexml in foodxml.findall("name"):
        if (foodxml.get("name")==foodxml and 
            foodxml.get("description")== descriptionxml):
            print("Ya existe este plato")
            return
    #creamos el nuevo plato
    nuevo_plato = ET.Element(name = namexml, price = pricexml,
                             description = descriptionxml, calories = caloriesxml)
    #Lo guardamos
    foodxml.append(nuevo_plato)
    tree.write("menuDesayuno.xml")
    return f"Plato Aniadido"


def buscarPrecio(name):
    root = cargarMenu()
    for food in root.findall("food"):
        name=food.find("name").text
        if name.lower()==name.lower():
            return pricexml
    

def modificarPrecio(name, nuevoPrecio):
    tree, root = cargarMenu()
    for food in root.findall("food"):
        namexml = food.find("name").text 
        if name.lower()==name.lower():
            #actualizar el precio
            food.find("price").text = str (nuevoPrecio)
            #guardamos los cambios
            tree.write("menuDesayuno.xml")
            return f"El precio ha sido actualizado"

def platoMasCaro():
    root = cargarMenu()
    precioMasAlto = 0
    