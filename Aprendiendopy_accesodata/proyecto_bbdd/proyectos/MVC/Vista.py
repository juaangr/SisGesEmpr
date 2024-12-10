

class vista_Gestion_Proyectos:
    
    def encabezado(self,mensaje):
        print(f'\n---------------------------------- {mensaje} ----------------------------------\n')
        
    def menu_principal(self):
        print("                          Introduzca 1 para iniciar programa")
        print("                          Introduzca 0 para salir del programa \n")
    
    
    
    def menu_categorias(self):
        print("                           Introduzca 1 para Gestion de Usuarios\n",
              "                          Introduzca 2 para Gestion de Departamentos\n",
              "                          Introduzca 3 para Gestion de Proyectos\n",
              "                          Introduzca 0 para salir del Menu Categorias \n")
    

    def menu_operaciones(self, operacion):
        print(f"                           Introduzca 1 para Aniadir {operacion}\n",
              f"                          Introduzca 2 para Eliminar {operacion}\n",
              f"                          Introduzca 3 para Modificar {operacion} \n",
              f"                          Introduzca 4 para Buscar {operacion} \n",
              f"                          Introduzca 5 para Mostrar todo {operacion}\n",
              f"                          Introduzca 0 para salir del Menu Operaciones\n")



    def mostrar_mensaje(self,mensaje):
        print(f'\n                           {mensaje}                            \n')



    def menu_confirmacion(self,mensaje):
        print(f'\n                           1 para confirmar {mensaje}\n',
              f'                           0 para abortar {mensaje}\n')
        
        
    def mostrar_error(self,error):
        print(f"                           Error: {error}")