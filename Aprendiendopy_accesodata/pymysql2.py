import pymysql
import sys

print("Empezamos")
try:
    conn = pymysql.connect(
        user = "root",
        password = "",
        host = "localhost",
        port = 3306,
        #db = "prueba2"
    )
except pymysql.Error as e:
    print(f"Error al conectarse: {e}")
    sys.exit(1)

# Cursor
cur = conn.cursor()
cur.execute("drop database if exists prueba2")
cur.execute("create database if not exists prueba2")


cur.execute("drop table if exists Persona")
cur.execute("""CREATE TABLE Persona (
    PersonID integer NOT NULL AUTO_INCREMENT,
    nombre varchar(25) not null,
    apellidos varchar(50) NOT NULL,
    telefono varchar(15) unique,
    edad int,
    primary key (personid),
    CHECK (edad>=1)
    )""")



cur.close()
conn.close()

# cur.execute("use prueba1")