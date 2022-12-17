#clase y estatico

#metodos de clase

class Pastel:
  def __init__(self,ingredientes):
    self.ingredientes=ingredientes

  def __repr__(self):
    return f'Pastel({self.ingredientes !r})' #utilizamos el __repr__ para que lea las variables o parametro tal y como son, no como __str__ que solo eran string
  
  @classmethod
  def PastelChocolate(cls): #los metodos de clases y utilizan el parametro cls
    return cls(['harina','leche','chocolate'])
  
  @classmethod
  def PastelVainilla(cls):
    return cls(['harina','leche','vainilla'])

print(Pastel.PastelChocolate())

#metodos estaticos
import math

class Pastel:
  def __init__(self,ingredientes,tamaño):
    self.ingredientes=ingredientes
    self.tamaño=tamaño
  
  def __repr__(self):
    return f'Pastel({self.ingredientes !r}, {self.tamaño}'

  def area(self):
    return self.tamañoArea(self.tamaño)
  
  @staticmethod
  def tamañoArea(A):
    return A**2 * math.pi

nuevoPastel=Pastel(['harina','azucar','lehce','crema'],4)

print(nuevoPastel.ingredientes)
print(nuevoPastel.tamaño)
print(nuevoPastel.tamañoArea(4))