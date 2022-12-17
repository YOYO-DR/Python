#metodos

class Matematica:
  def suma(self):
    self.n1=2
    self.n2=3

s=Matematica()
s.suma()
#print(s.n1+s.n2)

#constructor __init__(self)

class Ropa:
  def __init__(self):
    self.marca='willow'
    self.talla='M'
    self.color='rojo'

camisa=Ropa()
print(camisa.talla) #no necesito ejecurar la funcion pq la funcuin __init__ se auto ejecuta y asi puedo acceder a los valores sin necesidad de llamar la funcion
print(camisa.marca)

class Calculadora:
  def __init__(self,n1,n2):
    self.suma=n1+n2
    self.resta=n1-n2
    self.producto=n1*n2
    self.division=n1/n2

operacion=Calculadora(10,3)
print(operacion.producto)
print(operacion.suma)