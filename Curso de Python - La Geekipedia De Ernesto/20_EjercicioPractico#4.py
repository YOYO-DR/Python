print("\nCalculadora con una sola variable\n")
print("********************")
print("* Menú de opciones *")
print("********************")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División entera\n6. Exponente\n7. Modulo o resto\n")

numero=float(input("Introduce la opción deseada:"))
if numero==1:
  print("Elegiste suma\n")
  numero=int(input("Introduce el primer número:"))
  numero+=int(input("Introduce el segundo número:"))
  print("El resultado de la suma es:",numero)
elif numero==2:
  print("Elegiste resta\n")
  numero=int(input("Introduce el primer número:"))
  numero-=int(input("Introduce el segundo número:"))
  print("El resultado de la resta es:",numero)
elif numero==3:
  print("Elegiste multiplicación\n")
  numero=int(input("Introduce el primer número:"))
  numero*=int(input("Introduce el segundo número:"))
  print("El resultado de la multiplicación es:",numero)
elif numero==4:
  print("Elegiste división\n")
  numero=float(input("Introduce el primer número:"))
  numero/=float(input("Introduce el segundo número:"))
  print("El resultado de la división es:",round(numero,2))
elif numero==5:
  print("Elegiste división entera\n")
  numero=int(input("Introduce el primer número:"))
  numero//=int(input("Introduce el segundo número:"))
  print("El resultado de la división entera es:",numero)
elif numero==6:
  print("Elegiste exponente\n")
  numero=int(input("Introduce el primer número:"))
  numero**=int(input("Introduce el segundo número:"))
  print("El resultado de la potencia entera es:",numero)
elif numero==7:
  print("Elegiste modulo\n")
  numero=int(input("Introduce el primer número:"))
  numero%=int(input("Introduce el segundo número:"))
  print("El resultado de la potencia entera es:",numero)
else:
  print("La opcion no exite")