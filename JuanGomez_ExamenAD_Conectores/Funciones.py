def menuPrincipal(self):
        salir=False
        while(not salir):
            
            try:
                print("Menu principal")
                opcion = int(input())
                if (opcion==1):
                    self.menuOperaciones()
                    
                elif(opcion==0):  
                    print("Saliendo del programa...")
                    salir=True
                    
                else: 
                    print("Elige una opcion adecuada")  
                            
            except ValueError as ve:
                print("Elige una opcion adecuada")    
    
def menuOperaciones(self,): 
    salir=False
    while(not salir):
        try:
            print("Menu Operaciones")
            opcion = int(input())                
            if (opcion==1):
                funcAniadir()
                    
            elif(opcion==2):
                funcMostrarVentas()
                    
            elif(opcion==3):
                funcMostrarNoVendido()
                
            elif(opcion==4):
                salir=True
            
            else:   
                print("Elige una opcion valida")  
                
                
        except ValueError as ve:
            print("Elige una opcion valida")  
    
        
        
    def intentosCampo(self, funcCampo):
        intentos = 5
        while(intentos>0):
            
            campoIntroducido = funcCampo()
            if campoIntroducido:
                return True
            else:
                intentos -= 1
                print("No valido. Introduzca algo valido")
                
                if(intentos>=1):
                    print(f"Le restan {intentos} intentos.")
                    if(intentos==1):
                        print(f"Ultima oportunidad")
                
                elif(intentos==0):
                    return False
                
def funcAniadir(conection):
    try:
        cursor = conection.cursor()
        query = "INSERT INTO discos () VALUES ()"
        cursor.execute(query, (idDisco, titulo, autor, formato,  ))
        conection.commit()
        print(f"insertado exitosamente")
    except sqlite3.IntegrityError as e:
        print(f"Error al insertar: {e}")
    except sqlite3.Error as e:
        print(f"Error al insertar: {e}")
    
def funcMostrarNoVendido():
    pass
    
def funcMostrarVentas():
    pass