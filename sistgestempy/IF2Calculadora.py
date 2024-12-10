import sys
import math

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Este programa necesita 2 o 3 argumentos. Ejemplo de uso:")
        print("python calculadora.py 5 3 sumar")
        print("python calculadora.py 9 raiz")
        return

    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            operation = sys.argv[3].lower()

            if operation == "sumar":
                print(num1 + num2)
            elif operation == "restar":
                print(num1 - num2)
            elif operation == "multiplicar":
                print(num1 * num2)
            elif operation == "dividir":
                if num2 == 0:
                    print("Error: No se puede dividir entre 0.")
                else:
                    print(num1 / num2)
            else:
                print("Argumentos incorrectos.")
        except ValueError:
            print("Argumentos incorrectos.")
    
    elif len(sys.argv) == 2:
        try:
            num1 = float(sys.argv[1])
            option = sys.argv[2].lower()

            if option == "raiz" or option == "r":
                if num1 < 0:
                    print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
                else:
                    print(math.sqrt(num1))
            elif option == "cuadrado" or option == "c":
                print(num1 ** 2)
            else:
                print("Argumento incorrecto.")
        except ValueError:
            print("Argumentos incorrectos.")

if __name__ == "__main__":
    main()
