import sqlite3

# Aqui se encuentran los métodos que crean la base de datos junto las tablas 
def conectionDB(nombre_db):
    """Conecta a la base de datos SQLite y maneja errores."""
    try:
        conection = sqlite3.connect(nombre_db)
        print(f"Conectado a la base de datos '{nombre_db}' exitosamente")
        return conection
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crearTablaDiscos(conection):
    """Crea una tabla y maneja errores"""
    try:
        cursor = conection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXIST discos(
                            id INTEGER PRIMARY KEY
                            titulo TEXT NOT NULL
                            autor TEXT NOT NULL 
                            formato TEXT NOT NULL
                            anio INTEGER 
                            tipoMusica TEXT NOT NULL
                            precioDisco INTEGER
                            )"""
                            )
        conection.commit()
        print("Tabla 'discos' ya creada o existente")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla")


def crearTablaVentas(conection): 
    cursor = conection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXIST ventas (
                       id INTEGER PRIMARY KEY
                       discoVendido TEXT NOT NULL
                       cantidadDisco INTEGER NOT NULL
                       dniCliente INTEGER PRIMARY KEY
                       precioTotal INTEGER NOT NULL
                       )"""
                   )
