""" def saludo():
  print('Hola a todos')

#saludo()

def calculo():
  valor1=int(input('Ingresa el primer valor: '))
  valor2=int(input('Ingresa el segundo valor: '))
  total=valor1+valor2
  print(f'El total es: {total}')

#calculo()

#Funciones con parametro

def saludar(saludo):
  print(saludo) """

#saludar('Hola a todos!')

def calculo(valor1,valor2):
  total=valor1+valor2
  print(f'El total es: {total}')

calculo(20,30)