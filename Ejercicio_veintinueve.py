# Construya un generador que vaya recorriendo la sucesión aritmética: 1, 
# 2, 3, 4, 5 … Imprima por pantalla los 10 primeros valores.


def sucesion_aritmetica(n):
    numeros = []
    numero = 1
    for _ in range(n):
        numeros.append(numero)
        numero += 1
    return numeros
    
primeros_valores = sucesion_aritmetica(10)

print(primeros_valores)