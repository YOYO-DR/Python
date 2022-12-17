class Auto:
  def __init__(self,marca,color,ruedas):
    self.marca = marca
    self.color = color
    self.ruedas = ruedas
class Caracteristicas:
  def __init__(self):
    self.vehiculo=Auto('KAWASAKI','rojo',2) #creo un atributo que a la vez es un objeto de la clase "Auto"
    print('Datos del vehiculo')
    print(f'Marca: {self.vehiculo.marca}\nColo: {self.vehiculo.color}\nRuedas: {self.vehiculo.ruedas}')
    if self.vehiculo.ruedas==1:
      print('El vehiculo es un monociclo')
    elif self.vehiculo.ruedas==2:
      print('El vehiculo es una moto')
    elif self.vehiculo.ruedas==3:
      print('El vehiculo es un triciclo')
    elif self.vehiculo.ruedas==4:
      print('El vehiculo es un carro')
    elif self.vehiculo.ruedas>4:
      print('El vehiculo es un camion')

objeto=Caracteristicas()