class Leon:
  def tipoAnimal(self):
    print('\nAnimal de la familia de los felinos')

class Ballena:
  def tipoAnimal(self):
    print('\nAnimal de la familia de los cetáceos')

class Caballo:
  def tipoAnimal(self):
    print('\nAnimal de la familia de los equinos')

#metodo polimorfo
def animales(definicion):
  definicion.tipoAnimal()

animal=Caballo()
animales(animal)