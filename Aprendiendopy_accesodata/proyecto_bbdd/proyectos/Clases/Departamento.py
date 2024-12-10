from Assets import recursos as rec


class Departamento:
    __nombre = ''
    __descripcion = ''
    __responsable = None
  
  
  
    def set_nombre(self)->bool:
            input_nombre = input("                           Introduce nombre: ")
            
            if(input_nombre and rec.es_alfabetico(input_nombre)):
                self.__nombre = input_nombre.lower().title()
                return True
            
            else: 
                return False
            
    
    
    
    def set_descripcion(self)->bool:
            input_descripcion = input("                           Introduce descripcion: ")
            
            if(input_descripcion and rec.es_alfabetico(input_descripcion)):
                self.__descripcion = input_descripcion.lower().capitalize()
                return True
            
            else: 
                return False
    


    def set_responsable(self, func_leer_empleados)->bool:
        
        input_responsable = input("                           Introduce responsable de departamento: ")
        
        if(input_responsable and rec.es_alfabetico(input_responsable)):
            nombre_responsable = input_responsable.lower().title()
            query = (f'SELECT id_empleado, nombre_completo FROM empleados WHERE nombre_completo = {nombre_responsable}')
            empleados = func_leer_empleados(query)
            
            if(empleados[0] and empleados[0][1]==nombre_responsable):
                self.__departamento = empleados[0][0]
                return True
                
            else: 
                return   
        else: 
            return False
        
        

    def get_nombre(self):
        return self.__nombre
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_responsable(self):
        return self.__responsable