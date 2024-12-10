# la tienda se compone de los discos y ventas

# Discos; Titulo / autor // 
# formato (CD;DVD;VINILO;CASETTE) / año //
# Tipo de música (Pop/Rock/..) / precio  stock

# CRUD de discos -> crear, eliminar,
# mod., buscar y mostrar 
# otra funcionalidad para añadir stock para cuando se compren más uds
# antes d borrar y mod pide una confirmacion al usuario (para todo)

# Ventas; Los discos vendidos y su cant, el DNI del comprador
# hora y fecha al momento de la compra y el precio total 

# Antes de realizar la compra se verifica que las uds de cada disco
# estan disponibles, calcular y mostrar el precio total de la compra
# Se pide la confirmacion antes de realizar la compra
# una vez hecha, el stock debe actualizarse
# las ventas se crean y se muestran unicamente NO SE MOD NI BORRAN
# Lo mencionado son los minimos, + es mejor!

# Consideraciones:
# Si se introduce un campo no valido, se debe pedir de nuevo
# Si se introduce mal el dato 5 veces 
# se aborta la operacion y vuelve al submenu en cuestion
# Cada submenu tiene la opcion de volver al anterior
# solo se sale del mismo si el usuario ASI LO DESEA
# No podra haber discos repetidos (mismo titulo, autor y año)
# Modificar solo podra modificar un campo (al que debemos obligar a elegir
# al usuario), en caso de querer modificar todos los campos 
# se pedira confirmacion 
# el programa creará los ficheros que necesita, no funcionará a partir
# de archivos externos
# CODIGO INTENSAMENTE COMENTADO; CADA VARIABLE PARA QUE SE USA,
# ESTRUCTURA DE CONTROL UN COMENTARIO EN SU CABECERA,
# CADA METODO LO QUE HACE, QUE RECIBE Y QUE DEVUELVE.