#polimorfismo

""" class Auto:
  rueda=4
  def desplazamiento(self):
    print('El auto se esta desplazando sobre 4 ruedas')

class Moto:
  rueda=2
  def desplazamiento(self):
    print('La moto se esta desplazando sobre 2 ruedas') """

class Animales:
  def __init__(self,nombre):
    self.nombre=nombre
  def tipoAnimal(self):
    pass

class Leon(Animales):
  def tipoAnimal(self):
    print('Animal salvaje')

class Perro(Animales):
  def tipoAnimal(self):
    print('Animal domestico')

nuevoAnimal=Leon('Simba')
nuevoAnimal.tipoAnimal()

nuevoAnimal2=Perro('Rex')
nuevoAnimal2.tipoAnimal()