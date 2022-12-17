#Metodo super()
class Mamifero:
  def __init__(self,nombre):
    print(f'{nombre} es un animal de sangre caliente')

class Leon(Mamifero):
  def __init__(self):
    print('El leon es un animal de 4 patas')
    super().__init__('Simba') #lo utilizo para llamar algun metodo de la clase padre pero tambien para dar enfasis en esta clase que en la clase padre
  
nuevoLeon=Leon()