# Crear una lista con los días de la semana. Eliminar de la lista el sábado y 
# el domingo. Mostrar el contenido de la lista con un único print.

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

dias_semana.remove("Sábado")
dias_semana.remove("Domingo")


print("Días hábiles: ", dias_semana)