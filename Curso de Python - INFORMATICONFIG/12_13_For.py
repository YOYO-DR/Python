""" for f in range(10):
  print('Valor de f:',f)

#Ejemplo bucle while
f=0
while f<10:
  print(f)
  f+=1 """

""" for f in range(10,30,2):
  print('Valor de f:',f) """

""" suma=0
for i in range(10):
  valor=int(input('Ingrese valor: '))
  suma+=valor

promedio=suma/10
print('La suma es: ',suma)
print('El promedio es:',promedio) """

""" for i in 'Python':
  print(i) """


#Video 13

#Control de arroba

""" arroba = '@'
cantidad=0
mail=input('Ingrese su mail: ')
for i in mail:
  if i=='@':
    cantidad+=1
    
if cantidad>=1:
  print('Mail correcto')
else:
  print('Mail incorrecto, no tiene arroba')
 """

#tabla de multiplicar

valor = int(input('Indique el valor de la tabla: '))
print('Eligio ver la tabal del', valor)
for f in range(11):
  print(valor,'X',f,'=',f*valor)