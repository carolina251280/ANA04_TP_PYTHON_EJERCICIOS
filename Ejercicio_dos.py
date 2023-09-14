# Pidan el ingreso de dos datos a por teclado. Convierta los datos a flotantes 
# Muestre por pantalla los datos ordenados de menor a mayor.

num1= float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 < num2:
    print ("Los números ingresados son: ", num1, ", ", num2 )
else:
    print ("Los números ingresados son: ", num2, ", ", num1 )