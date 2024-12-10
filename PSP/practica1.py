#con este programa pasaremos de fh a celsius y viceversa
# C = (F- 32) / 1.8
fahrenheit = 32
celsius = 0

def formulaCelAfh(fahrenheit):
    celsius_n = (fahrenheit - 32) / 1.8    
    return celsius_n

def formulaFhAcel(celsius):
    fahrenheit_n = (1.8 * celsius) + 32
    return fahrenheit_n