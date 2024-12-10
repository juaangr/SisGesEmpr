import pymysql

class Modelo_Gestion_Proyectos:
    
    def __init__(self) -> None:
        self.crear_BBDD_y_tablas()

        
    def conexion_BBDD(self, database=None):
        conn = None
        
        try:
            conn = pymysql.connect(
                user="root",
                password="",
                host="localhost",
                port=3306,
                db=database  
            )
            
            return conn
        
        
        except pymysql.Error as e:
            return False
        
        ''' finally:
            if conn:
                conn.close()'''
            


    def crear_BBDD_y_tablas(self)->bool:
        
        connexion = self.conexion_BBDD()
        
        if(connexion):
            try:
                cursor = connexion.cursor()
                
                
                cursor.execute("CREATE DATABASE IF NOT EXISTS Gestion_Proyectos;")
                cursor.execute("USE Gestion_Proyectos;")
                
                 # Crear tabla departamentos sin la clave foránea hacia empleados
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamentos (
                    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL,
                    descripcion TEXT,
                    id_empleado_responsable INT DEFAULT NULL
                );
                """)

                # Crear tabla empleados sin la clave foránea hacia departamentos
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
                    nombre_completo VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    cargo VARCHAR(50),
                    fecha_contratacion DATE NOT NULL,
                    salario DECIMAL(10, 2),
                    id_departamento INT
                );
                """)

                # Crear tabla proyectos sin las claves foráneas hacia departamentos y empleados
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyectos (
                    id_proyecto INT PRIMARY KEY AUTO_INCREMENT,
                    nombre VARCHAR(100) NOT NULL,
                    descripcion TEXT,
                    fecha_inicio DATE NOT NULL,
                    fecha_fin DATE,
                    id_departamento INT,
                    id_empleado_jefe INT
                );
                """)

                # Crear tabla empleados_proyectos sin las claves foráneas
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados_proyectos (
                    id_empleado INT,
                    id_proyecto INT,
                    PRIMARY KEY (id_empleado, id_proyecto)
                );
                """)

                # Ahora agregar las claves foráneas usando ALTER TABLE
                cursor.execute("""
                ALTER TABLE departamentos
                ADD CONSTRAINT fk_empleado_responsable
                FOREIGN KEY (id_empleado_responsable) REFERENCES empleados(id_empleado);
                """)

                cursor.execute("""
                ALTER TABLE empleados
                ADD CONSTRAINT fk_departamento
                FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento);
                """)

                cursor.execute("""
                ALTER TABLE proyectos
                ADD CONSTRAINT fk_departamento_proyecto
                FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento);
                """)

                cursor.execute("""
                ALTER TABLE proyectos
                ADD CONSTRAINT fk_empleado_jefe
                FOREIGN KEY (id_empleado_jefe) REFERENCES empleados(id_empleado);
                """)

                cursor.execute("""
                ALTER TABLE empleados_proyectos
                ADD CONSTRAINT fk_empleado
                FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado);
                """)

                cursor.execute("""
                ALTER TABLE empleados_proyectos
                ADD CONSTRAINT fk_proyecto
                FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto);
                """)
                
                connexion.commit()

                return True
            
            except pymysql.Error as e:
                #print(f"Error al crear tablas: {e}")
                return False

            finally:
                if connexion:
                    cursor.close()
                    connexion.close()
                    #print("Conexión cerrada correctamente.")
        
        else:      
            return False
        
    
    
    
    
    def cant_entradas_tabla(self, nomTabla)->bool:
        coneccion = self.conexion_BBDD('Gestion_Proyectos')
        
        if coneccion: 
            
            try:
                cursor = coneccion.cursor()
                cursor.execute(f"SELECT COUNT(*) FROM {nomTabla}")
                num_entradas = cursor.fetchone()
                #coneccion.commit() # used to confirm the changes made by the user to the database. En este caso no lo uso porque sleect no hace cambios
                
                return num_entradas
                
            except pymysql.Error as e:
                return False
            
            finally: 
                if coneccion:
                    cursor.close()
                    coneccion.close() 
        
        else: 
            return False
        
        
        
        
        
    
    def leer(self, query)->tuple:
        
        coneccion = self.conexion_BBDD('Gestion_Proyectos')
        
        if coneccion: 
            
            try:
                cursor = coneccion.cursor()
                cursor.execute(query)
                filas = cursor.fetchall()
                coneccion.commit()
                
                return filas
                
            except pymysql.Error as e:
                return False
            
            finally: 
                if coneccion:
                    cursor.close()
                    coneccion.close() 
        
        else: 
            return False
         
         
         
    def insertar_empleado(self, tupla_campos):
        coneccion = self.conexion_BBDD('Gestion_Proyectos')
        
        if coneccion: 
            
            try:
                cursor = coneccion.cursor()
                query = "INSERT INTO empleados (nombre_completo, email, cargo, fecha_contratacion, salario, id_departamento) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor.execute(query, tupla_campos)
                coneccion.commit()
                
                return True
                
            except pymysql.Error as e:
                return False
            
            finally: 
                if coneccion:
                    cursor.close()
                    coneccion.close() 
                    
                    
                    
   
    def insertar_departamento(self, tupla_campos):
        coneccion = self.conexion_BBDD('Gestion_Proyectos')
        
        if coneccion: 
            try:
                cursor = coneccion.cursor()
                query = "INSERT INTO departamentos (nombre, descripcion, id_empleado_responsable) VALUES (%s, %s, %s);"
                cursor.execute(query, tupla_campos)
                coneccion.commit()
                
                return True
                
            except pymysql.Error as e:
                return False
            
            finally: 
                if coneccion:
                    cursor.close()
                    coneccion.close()
    
    def insertar_proyecto(self):
        pass