print("\nSistema para saber que numero es mayor\n")
numUno=int(input("Ingresa el primer numero: "))
numDos=int(input("Ingresa el segundo numero: "))
numTres=int(input("Ingresa el tercer numero: "))

if numUno>numDos and numUno>numTres:
  print("El número",numUno,"es el más grande de los 3")
elif numDos>numTres:
  print("El número",numDos,"es el más grande de los 3")
else:
  print("El número",numTres,"es el más grande de los 3")