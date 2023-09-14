# Crear una tupla con los siete días de la semana. Recorrer los 365 días del 
# año 2023. Para cada día del año imprimir el nombre del día de la semana.

import calendar
import datetime

dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
año = 2023

for mes in range(1, 13):  
    for dia in range(1, calendar.monthrange(año, mes)[1] + 1):  
        fecha = datetime.date(año, mes, dia)
        numero_dia_semana = fecha.weekday()  
        nombre_dia = dias_semana[numero_dia_semana]
        print(f"{dia}/{mes}/{año} es un día {nombre_dia}")