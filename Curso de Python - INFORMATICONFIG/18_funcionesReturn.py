#Funcion calcular area de un triangulo
""" def triangulo(base,altura):
  area=base*altura/2
  return area

base=int(input('Ingresa la base: '))
altura=int(input('INgrese la altura: '))

print(f'El area del triangulo es: {triangulo(base,altura)}') """

#funcion calcular mayor valor
def mayorValor(valor1,valor2):
  if valor1>valor2:
    mayor=valor1
  else:
    mayor=valor2
  return mayor

#bloque principal
v1=int(input('Ingrese el primer valor: '))
v2=int(input('Ingrese el segundo valor: '))

print(f'El mayor valor es: {mayorValor(v1,v2)}')