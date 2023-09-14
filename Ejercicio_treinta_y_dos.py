# Construya un generador que vaya recorriendo la suma de la serie 
# geométrica: 1, 3, 7, 15, 31, 63, 127 Imprima por pantalla los 10 primeros 
# valores

def serie_suma_geometrica(n):
    numeros = []
    numero_actual = 1
    for _ in range(n):
        numeros.append(numero_actual)
        numero_actual = numero_actual * 2 + 1
    return numeros

primeros_valores = serie_suma_geometrica(10)

print(primeros_valores)