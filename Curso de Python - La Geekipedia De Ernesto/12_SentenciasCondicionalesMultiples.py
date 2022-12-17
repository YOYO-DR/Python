'''
numUno=3
if numUno==1:
    print("El número es UNO.")
elif numUno==2:
    print("El número es DOS.")
else:
    print("El número se desconoce.")
print("Fin.")
'''
print("===================================")
print("¡¡Convertidos de números a letras!!")
print("===================================")

num=int(input("¿Cúal es el número que deseas convertir?: "))
if num==0:
    print("El número es 'Cero'")
elif num==1:
    print("El número es 'Uno'")
elif num==2:
    print("El número es 'Dos'")
elif num==3:
    print("El número es 'Tres'")
elif num==4:
    print("El número es 'Cuatro'")
elif num==5:
    print("El número es 'Cinco'")
else:
    print("Este programa solo puede convertir hasta el número 5 (",num,", no registrado)")
print("Fin.")