# Crear una lista l1 con todos los días de la semana Imprimir la longitud de 
# l1. Extender l1 con si misma Imprimir la longitud de l1.

l1 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Longitud de l1 :", len(l1))

l1.extend(l1)

print("Longitud de l1 extendida :", len(l1))