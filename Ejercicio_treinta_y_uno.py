# Construya un generador que vaya recorriendo la serie geométrica: 1, 2, 4, 
# 8, 16, 32, 64 … Imprima por pantalla los 10 primeros valores.

def serie_geometrica(n):
    numeros = []
    numero_actual = 1
    for _ in range(n):
        numeros.append(numero_actual)
        numero_actual *= 2
    return numeros

primeros_valores = serie_geometrica(10)
print(primeros_valores)