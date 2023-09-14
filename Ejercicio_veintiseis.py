# Crear una tupla con las longitudes de los meses del año 2023. Recorrer 
# el año mostrando por pantalla el número de día dentro del año y el número 
# del día dentro del mes.

año = 2023

longitudes_meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

dia_del_año = 1
mes_actual = 1

for longitud_mes in longitudes_meses:
    for dia_mes in range(1, longitud_mes + 1):
        print(f"Día {dia_del_año} del año {año} - Día {dia_mes} del mes {mes_actual}")
        dia_del_año += 1
    mes_actual += 1