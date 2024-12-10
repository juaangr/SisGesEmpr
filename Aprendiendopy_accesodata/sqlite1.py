import sqlite3

#agenda con contactos (nombre compl, teléfono, edad)
# esta va a ser la conexion a la base de datos agenda1
conn = sqlite3.connect('agenda1.db')
print("Base de datos abierta con exito")

# este va a ser nuestro cursor que sirve para interactuar con la db
cursor = conn.cursor()

# creamos una tabla con los atr; Nombre, apellidos, telefono y edad
comando1 = """CREATE TABLE IF NOT EXISTS
agenda (nombre TEXT, apellidos TEXT, telefono INTEGER PRIMARY KEY, edad INTEGER)"""


def insertAtr():
    # la siguiente linea ejecuta el comando1
    cursor.execute(comando1)

    # aqui vamos a añadir las personas de nuestra agenda
    cursor.execute("INSERT INTO agenda VALUES ('Juan', 'Gomez', 650449573, 20)")
    cursor.execute("INSERT INTO agenda VALUES ('Anouar', 'Tahiri', 623897456, 19)")
    cursor.execute("INSERT INTO agenda VALUES ('Bruno','Berria', 679224630, 19)")
    print("Tabla creada")

    # datos = cursor("show tabbles")
    conexion.commit()
    cursor.close()
    conexion.close()

def mostrarCosas():
    