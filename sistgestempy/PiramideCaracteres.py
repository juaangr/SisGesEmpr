# vamos a realizar una piramide de carácteres  pidiendo el caracter por pantalla
# vamos a usar el formato: fstring() ^^^^^

# Recursos que vamos a utilizar
numLineas = 7
caracter = "A"

# bucle for que va a gestionar 
for i in range(1, numLineas + 1):
    totalBase = 2 * numLineas - 1
    caracteres = caracter * (2 * i - 1)
    print("{:^{width}}".format(caracteres, width=totalBase))
