#Conjunción
print("\nConjunción (and)")

numUno=int(input("Escribe un número mayor a 2 y menor a 5: "))

if numUno>2 and numUno <5:
  print("El número",numUno,"cumple con la condicion.\n")
else:
  print("El número",numUno,"NO cumple la condición")

#disyunción
print("\nDisyunción (or)")
palabra=input("Para cumplir con la condición escribe 'si' o 'yes': ")
palabra=palabra.lower()
if palabra=="si" or palabra=='yes':
  print("La condición se ha cumplido")
else:
  print("La condición NO se ha cumplido")

#negación
print("\nNegación (not)")

numUno=int(input("Introcuce un numero igual a 5: "))

if not numUno==5:
  print("El número es diferente de cinco y si cumple la condición")
else:
  print("El número es igual a cinco y NO cumple la condición")