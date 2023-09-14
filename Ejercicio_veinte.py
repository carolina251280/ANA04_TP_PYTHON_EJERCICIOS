# Crear una tupla con la siete primeras letras del alfabeto. Recorrer la tupla 
# y usarla como clave para imprimir los valores del diccionario construido 
# en el ejercicio 19.

t1 = ("a", "b", "c", "d", "e", "f", "g")
dias_semana= {'a': "Lunes", 'b': "Martes", 'c': "Miércoles", 'd': "Jueves", 'e': "Viernes", 'f': "Sábado", 'g': "Domingo"}


for x in t1:
    print(dias_semana[x])