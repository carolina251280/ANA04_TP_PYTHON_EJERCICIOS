# Tomar el diccionario generado en el ejercicio 19 y cambiar cada valor 
# letras mayúsculas. Imprimir el resultado.

dias_semana= {'a': "Lunes", 'b': "Martes", 'c': "Miércoles", 'd': "Jueves", 'e': "Viernes", 'f': "Sábado", 'g': "Domingo"}

for x in dias_semana:
    dias_semana[x] = dias_semana[x].upper()

print(dias_semana)