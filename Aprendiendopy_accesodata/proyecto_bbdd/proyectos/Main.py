from MVC import Controlador, Modelo, Vista

 

model = Modelo.Modelo_Gestion_Proyectos()
vist = Vista.vista_Gestion_Proyectos()
control = Controlador.Controlador_Gestion_Proyectos(model, vist)

control.menu_principal()