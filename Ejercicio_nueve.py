# Crear una lista con los días hábiles de la semana y otra lista con el sábado 
# y el domingo. Extender la primera lista con la segunda. Mostrar el 
# contenido de la lista con un único print.

dias_habiles = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

fin_de_semana = ["Sábado", "Domingo"]

dias_habiles.extend(fin_de_semana)

print("Días de la semana:", dias_habiles)