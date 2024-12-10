def realizar_operacion():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("Introduce la operación (sumar, restar, multiplicar, dividir): ").lower()
    if operacion == "sumar":
        resultado = num1 + num2
    elif operacion == "restar":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: No se puede dividir entre 0."
    else:
        resultado = "Operación no válida"
    print(f"Resultado: {resultado}")

def calculadora():
    while True:
        realizar_operacion()
        respuesta = input("¿Quieres realizar otra operación? (SI/NO): ").lower()
        if respuesta == "no":
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            return
        elif respuesta != "si":
            print("Respuesta no válida. Saliré de la calculadora.")
            return
#para ejecutar la calculadora;
calculadora()