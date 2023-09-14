# Ingresar por teclado dos enteros y almacenarlos en a y b. Crear una 
# función de dos parámetros que devuelve la suma de esos parámetros 
# Usar la función creada para calcular la suma de a y b. Mostrar por pantalla 
# el resultado de la suma.

a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

def suma(x, y):
    return x + y


resultado = suma(a, b)

print("La suma de", a, " y ", b, "es igual a", resultado)