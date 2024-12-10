def tiene_digitos(cadena: str)->bool:
    for c in cadena:
        if c.isdigit():
            return True
    return False




def es_entero(cadena: str)->bool:
    try:
        int(cadena)
        return True
    except ValueError:
        return False
    
    
    
    
def es_numero_positivo(cadena: str)->bool:
    try:
        numero = float(cadena)
        return numero >= 0  # Asegura que no sea negativo
    except ValueError:
        return False
    
    
    

def es_alfabetico(cadena: str)->bool:
    import re
    
    patron = r'^[a-zA-Z]+$'
    return bool(re.match(patron, cadena))



def es_correo_valido(cadena: str) -> bool:
    import re
  
    patron = r'^[a-zA-Z0-9.@]+$'
    return bool(re.match(patron, cadena))


def fecha_valida(fecha: str) -> bool:
    from datetime import datetime
  
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
      
        return False