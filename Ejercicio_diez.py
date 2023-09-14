# Crear una lista l1 con todos los días de la semana. Crear una lista l2 con 
# los días hábiles de la semana. Recorrer l1 e indicar para cada elemento 
# si se encuentra o no en l2.

l1 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

l2 = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in l1:
    if dia in l2:
        print(dia," se encuentra en la lista de días hábiles.")
    else:
        print(dia," no se encuentra en la lista de días hábiles.")