# Ingresar por teclado una edad. Mostrar por los años todos los cumpleaños 
# que la persona tuvo hasta ahora: Cumpleaños 1 Cumpleaños 2.

edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("La edad debe ser un número positivo.")
else:
    for x in range(1, edad + 1):
        print("Cumpleaños", x)