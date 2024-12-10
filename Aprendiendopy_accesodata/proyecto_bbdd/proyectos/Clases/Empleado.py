import Assets.recursos as rec

class Empleado:
    __nombre_completo = ''
    __email = ''
    __cargo = ''
    __fecha_contratacion = ''
    __salario = 0
    __departamento = ''


    '''
        def __init__(self,nombre,apellido,email,cargo,fecha_contratacion,salario,departamento) -> None:
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__cargo = cargo
        self.__fecha_contratacion = fecha_contratacion
        self.__salario= salario
        self.__departamento = departamento #validar si existe el departamento introducido en base de datos
    
    '''
    
    # Métodos SET
    def set_nombre_completo(self)->bool:
            input_nombre_completo = input("                           Introduce nombre: ")
            
            if(input_nombre_completo and rec.es_alfabetico(input_nombre_completo)):
                self.__nombre_completo = input_nombre_completo.lower().title()
                return True
            
            else: 
                return False
            
            

        
        

    def set_email(self)->bool:
        
            input_email = input("                           Introduce email: ")
            
            if(input_email and rec.es_correo_valido(input_email)):
                self.__email  = input_email
                return True
            
            else: 
                return False
        
        
        
        

    def set_cargo(self)->bool:
        
            input_cargo = input("                           Introduce cargo: ")
            
            if(input_cargo and rec.es_alfabetico(input_cargo)):
                self.__cargo = cargo = input_cargo.lower().capitalize()
                return True
            
            else: 
                return False
        
        

    def set_fecha_contratacion(self)->bool:

            input_fecha = input("                           Introduce fecha(dd/mm/yyyy): ")
            
            if(input_fecha and rec.fecha_valida(input_fecha)):
                self.__fecha_contratacion = cargo = input_fecha
                return True
            
            else: 
                return False




    def set_salario(self)->bool:

            try:
                input_salario = float(input("                           Introduce salario: "))
                
                if(input_salario and input_salario > 0):
                    self.__salario = input_salario
                    return True
                
                else: 
                    return False
                
            except: 
                return False
        




    def set_departamento(self, funcion_leer_deptos):
        input_depto = input("                           Introduce departamento: ")
        
        if(input_depto and rec.es_alfabetico(input_depto)):
            nombre_depto = input_depto.lower().title()
            query = (f'SELECT id_departamento, nombre FROM departamentos WHERE nombre = {nombre_depto}')
            deptos = funcion_leer_deptos(query)
            
            if(deptos[0] and deptos[0][1]==nombre_depto):
                self.__departamento = deptos[0][0]
                return True
                
            else: 
                return   
        else: 
            return False
        

    
    
    # Métodos GET
    def get_nombre_completo(self):
        return self.__nombre


    def get_email(self):
        return self.__email

    def get_cargo(self):
        return self.__cargo

    def get_fecha_contratacion(self):
        return self.__fecha_contratacion

    def get_salario(self):
        return self.__salario

    def get_departamento(self):
        return self.__departamento


    def __str__(self):
        return (f"Nombre: {self.__nombre_completo} \n"
                f"Email: {self.__email}\n"
                f"Cargo: {self.__cargo}\n"
                f"Fecha de contratación: {self.__fecha_contratacion}\n"
                f"Salario: {self.__salario}\n"
                f"Departamento: {self.__departamento}")