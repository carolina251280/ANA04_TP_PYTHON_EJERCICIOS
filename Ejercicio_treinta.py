# Construya un generador que vaya recorriendo la serie que va sumando la 
# sucesión aritmética: 1, 2, 3, 6, 10, 15, 21 … Imprima por pantalla los 10 
# primeros valores.

def serie_suma_aritmetica(n):
    numeros = []
    numero_actual = 1
    suma = 0
    for _ in range(n):
        suma += numero_actual
        numeros.append(suma)
        numero_actual += 1
    return numeros

primeros_valores = serie_suma_aritmetica(10)
print(primeros_valores)