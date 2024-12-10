#import Modelo as mod
#import Vista as vis
from Clases import Empleado, Proyecto, Departamento


class Controlador_Gestion_Proyectos:
    
    def __init__(self,modelo_gestion_proyectos,vista_gestion_proyectos) -> None:
        self.modelo=modelo_gestion_proyectos
        self.vista=vista_gestion_proyectos
    
    
    
    
    #Menus
    def menu_principal(self):
        salir=False
        while(not salir):
            
            try:
                self.vista.encabezado("Menu principal")
                self.vista.menu_principal()
                opcion = int(input())
                
                if (opcion==1):
                    self.menu_categorias()
                    
                elif(opcion==0):  
                    self.vista.mostrar_mensaje("       ADIOOOOOOOOOOSSS!!!!")
                    salir=True
                    
                else: 
                    self.vista.mostrar_mensaje("Atencion!!! Escoja un numero entre los disponibles!!! ")  
                            
            except ValueError as ve:
                self.vista.mostrar_mensaje("Atencion!!! Escoja un numero entre los disponibles!!! ")  
            
            
            
            
    
        
    def menu_categorias(self):
        salir=False
        
        while(not salir):
            
            try:
                self.vista.encabezado("Menu Categorias")
                self.vista.menu_categorias()
                opcion = int(input())
                
                if (opcion==1):
                    self.menu_operaciones("Usuario", self.aniadir_empleado, self.eliminar_empleado, 
                        self.modificar_empleado,self.buscar_empleado,self.mostrar_todos_empleado )#pasarle por paramentros referencia alas funciones q el metodo dependiendo si se elige departamento, etc separ que operaciones realizar (aniadir_empleado, anidair_departamentyto, etc)

                elif(opcion==2):  
                    self.menu_operaciones("Departamento", self.aniadir_departamento, self.eliminar_departamento, 
                        self.modificar_departamento,self.buscar_departamento,self.mostrar_todos_departamento )
                    
                elif(opcion==3):  
                    self.menu_operaciones("Proyecto", self.aniadir_proyecto, self.eliminar_proyecto, 
                        self.modificar_proyecto,self.buscar_proyecto,self.mostrar_todos_proyecto)

                elif(opcion==0):  
                    salir=True
                    
                else:   
                    self.vista.mostrar_mensaje("Atencion!!! Escoja un numero entre los disponibles!!! ")  
                
                
            except ValueError as ve:
                self.vista.mostrar_mensaje("Atencion!!! Escoja un numero entre los disponibles!!! ")     
    
    
    
    def menu_operaciones(self, operacion: str, func_aniadir, func_eliminar, func_modificar, func_buscar, func_mostrar_todo ):#pasarle por parametyro
        salir=False
        while(not salir):
            try:
                self.vista.encabezado("Menu Operaciones")
                self.vista.menu_operaciones(operacion)
                opcion = int(input())
                
                if (opcion==1):# Aniadir disco a stock
                    func_aniadir()
                    
                elif(opcion==2):# Eliminar disco de stock
                    func_eliminar()
                    
                elif(opcion==3):# Modificar disco de stock  
                    func_modificar()
                
                elif(opcion==4):# Buscar cierto disco en stock  
                    func_buscar()
                    
                elif(opcion==5): # Mostrar todos los discos en stock
                    func_mostrar_todo()
            
                elif(opcion==0):  
                    salir=True
                    
                else:   
                    self.vista.mostrar_mensaje("Atencion!!! Escoja un numero entre los disponibles!!! ")  
                
                
            except ValueError as ve:
                self.vista.mostrar_mensaje("Atencion!!! Escoja un numero entre los disponibles!!! ")  
    
    
    
    
    #Metodos empleado
    def aniadir_empleado(self):
        #campo_anterior = False #variasble que validara pasar al almacenamiento del siguiente campo solo si se ha almacenado el valor precio correcto
        
        empleado = Empleado.Empleado()
        campo_correcto = self.intentos_campo(empleado.set_nombre_completo)#validar de el campo nombre ha sido correctamente almacenado en el objeto Empleadoç
            
        if(campo_correcto):
            campo_correcto = self.intentos_campo(empleado.set_email)
        
        if(campo_correcto):
            campo_correcto = self.intentos_campo(empleado.set_cargo)
        
        if(campo_correcto):
            campo_correcto = self.intentos_campo(empleado.set_fecha_contratacion)
            
        if(campo_correcto):
            campo_correcto = self.intentos_campo(empleado.set_salario)
            
            
            
        
        departamentos = None
        if campo_correcto :
            existen_departamentos = self.modelo.cant_entradas_tabla("departamentos")#cantidad de ENTRADAS en determinada tabla
            
            if existen_departamentos[0]!=0: #valida que haya algun departamento en la tabla departamento al que asignar al empleado
                campo_correcto = self.intentos_campo_opciones(empleado.set_departamento, self.modelo.leer)
            else:
                self.vista.mostrar_mensaje("Atencion!!! Operacion fallida. El campo de departamento de empleado no se puede realizar.")
                self.vista.mostrar_mensaje("No existen departamentos en base de datos.")
                self.vista.mostrar_mensaje("Ingrese algun departamento en base de datos y posteriorente intente crear un empleado.")
                campo_correcto = False
                
                
                
        if campo_correcto:
               #llamar al modelo para inroducir los datos del objeto empleado en su tabla correspondiente en abase de datos
            tupla_empleado = (empleado.get_nombre_completo, empleado.get_email, empleado.get_cargo, 
                              empleado.get_fecha_contratacion, empleado.salario, empleado.get_departamento)
            insertar = self.modelo.insertar_empleado(tupla_empleado)
            if insertar:
                self.vista.mostrar_mensaje("Se inserto entrada empleado en base de datos.")
            else:
                self.vista.mostrar_mensaje("NO se pudo insertar la entrada introducida en base de datos.")
            
        #print(empleado)   
                #print(f'empleado uintroduchi: {empleado.get_nombre()}')
    
    def eliminar_empleado(self):
        pass
    
    def buscar_empleado(self):
        pass
    
    def mostrar_todos_empleado(self):
        pass
    
    def modificar_empleado(self):
        pass
    
    def intentos_campo(self, func_campo)->bool: # Metodo que por parametro tiene una referencia a una funcion (en este caso les pase un metodo de un objeto Empleado ya )
        intentos = 5
        while(intentos>0):
            
            campo_introducido = func_campo()
            if campo_introducido:
                return True
            else:
                intentos -= 1
                self.vista.mostrar_mensaje("Atencion!!! El campo introducido no es valido. Introduzca otro correcto.")
                
                if(intentos>=1):
                    self.vista.mostrar_mensaje(f"Le restan {intentos} intentos.")
                    if(intentos==1):
                        self.vista.mostrar_mensaje(f"Ultima oportunidad, sino volvera al menu anterior.")
                
                elif(intentos==0):
                    return False
                
    
    
    
    def intentos_campo_opciones(self, func_campo, func_leer_modelo)->bool: # igual al metodo intentos_campo pero con la limitacion de que se deben almacenar los datos que vienen en la lista que se pasa por argumentos
        intentos = 5
        while(intentos>0):
            
            campo_introducido = func_campo(func_leer_modelo)
            if campo_introducido:
                return True
            else:
                intentos -= 1
                self.vista.mostrar_mensaje("Atencion!!! El campo introducido no es valido. Introduzca otro correcto.")
                
                if(intentos>=1):
                    self.vista.mostrar_mensaje(f"Le restan {intentos} intentos.")
                    if(intentos==1):
                        self.vista.mostrar_mensaje(f"Ultima oportunidad, sino volvera al menu anterior.")
                
                elif(intentos==0):
                    return False
            
        
        
    
    
    #Metodos departamento
    def aniadir_departamento(self):
        departamento = Departamento.Departamento()
        campo_correcto = self.intentos_campo(departamento.set_nombre)#validar de el campo nombre ha sido correctamente almacenado en el objeto Empleadoç
            
        if(campo_correcto):
            campo_correcto = self.intentos_campo(departamento.set_descripcion)
        
        
        #tupla_empleados = self.modelo.leer("SELECT nombre_completo FROM empleados;")
        
        if campo_correcto :
            existen_empleados = self.modelo.cant_entradas_tabla("empleados")
            
            if existen_empleados[0]==0: 
                self.vista.mostrar_mensaje("Atencion!!! El campo de responsable de departamento no se puede realizar.")
                self.vista.mostrar_mensaje("No existen empleados en base de datos.")
                
                lista_campos = [departamento.get_nombre, departamento.get_nombre,]
                entrada_aniadida = self.modelo.insertar(lista_campos)
                
                if entrada_aniadida:
                    self.vista.mostrar_mensaje("Se ha aniadido la entrada de departamento a base de datos.")
                    self.vista.mostrar_mensaje("Sin embargo, el campo responsable de dapartamento se aniadio como vacio (NULL).")
                    self.vista.mostrar_mensaje("Modifique el campo cuando haya departamentos disponibles.")
                    
            else:
                campo_correcto = self.intentos_campo_opciones(departamento.set_responsable, self.modelo.leer)
                
                if campo_correcto:
            
                    tupla_departamentos = (departamento.get_nombre, departamento.get_descripcion, departamento.get_responsable)
                    insertar = self.modelo.insertar_departamento(tupla_departamentos)
                    if insertar:
                        self.vista.mostrar_mensaje("Se inserto entrada departamento en cu integridad en base de datos.")
                    else:
                        self.vista.mostrar_mensaje("No se pudo insertar la entrada introducida en base de datos.")
                
        
       
            
                
        
    
            
            
            
    
    def eliminar_departamento(self):
        pass
    
    def buscar_departamento(self):
        pass
    
    def mostrar_todos_departamento(self):
        pass
    
    def modificar_departamento(self):
        pass
    
    
    
    #Metodos proyecto
    def aniadir_proyecto(self):
        pass
    
    def eliminar_proyecto(self):
        pass
    
    def buscar_proyecto(self):
        pass
    
    def mostrar_todos_proyecto(self):
        pass
    
    def modificar_proyecto(self):
        pass