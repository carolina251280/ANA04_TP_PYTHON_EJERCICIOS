# Generar una lista l1 con los números del 1 al 10. Generar una lista l2 que 
# tenga una lista con los números del uno al 10 en cada uno de sus 10 
# elementos. Recorrer l2 con un for anidado dentro de otro for mostrando el 
# producto de ambas coordenadas.

l1 = list(range(1, 11))
l2 = [list(range(1, 11))] *10
print(l2)

for fila in l2:
    for elemento in fila:
        producto = elemento * l1[elemento - 1]  
        print("Coordenadas", elemento, l1[elemento - 1], ": Producto = ", producto)
