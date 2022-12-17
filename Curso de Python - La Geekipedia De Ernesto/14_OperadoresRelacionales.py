print("\nIntroduce dos números a comparar:\n")
numUno=int(input("Introduce el primer número: "))
numDos=int(input("Introduce el segundo número: "))
print("\n Los números a comparar son:",numUno,"y",numDos,"\n")
if numUno!=numDos:
  print("Es diferente...")
else:
  print("Es igual...")
if numUno>numDos:
  print("Es mayor...")
else:
  print("No es mayor...")
if numUno>=numDos:
  print("Es mayor o igual...")
else:
  print("No es mayor o igual...")
print("Fin.")