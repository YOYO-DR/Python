#Ejemplo 1
nombre=input("¿Cúal es tu nombre?: ")
print("Hola "+nombre+", vamos a realizar una suma.")
numeroUno=int(input("porfavor introduce el primer valor: "))
numeroDos=int(input("porfavor introduce el segundo valor: "))
resultado=numeroUno+numeroDos
print(nombre+", el resultado de la suma es: ",resultado)

#Ejemplo 2
palabra=input("Introduce una palabra: ")
numInt=int(input("Introduce un numero entero: "))
numFloat=float(input("Introduce un numero flotante: "))
numComplex=complex(input("Introduce un numero complejo: "))

print("String:",palabra)
print("Entero:",numInt)
print("Flotante:",numFloat)
print("Número complejo:",numComplex)