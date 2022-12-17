#herencia ejemplo practico

class Calculadora:
  def __init__(self,numero):
    self.n=numero
    self.datos=[0 for i in range(numero)]
  
  def ingresarDato(self):
    self.datos=[int(input('ingresar datos '+str(i+1)+' = ')) for i in range(self.n)]

class OpBasicas(Calculadora):
  def __init__(self):
    Calculadora.__init__(self,2)
  
  def suma(self):
    a,b,=self.datos
    s = a+b
    print(f'El resultado es: {s}')

  
  def resta(self):
    a,b,=self.datos
    s = a-b
    print(f'El resultado es: {s}')


class Raiz(Calculadora):
  def __init__(self):
    Calculadora.__init__(self,1)
  
  def cuadrada(self):
    import math
    a,=self.datos
    print(f'El resultado es: {math.sqrt(a)}')


""" ejemplo=OpBasicas()
print(ejemplo.ingresarDato())
print(ejemplo.suma()) """

""" ejemplo=Raiz()
print(ejemplo.ingresarDato())
print(ejemplo.cuadrada()) """

numeros=[int(input(f'Ingresa el {i+1}° numero: ')) for i in range(10)]
#print(numeros)