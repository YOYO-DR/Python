#Clase_auto

class Auto:
  def __init__(self):
    self.marca='BMW'
    self.puertas=4
    self.color='rojo'
    self.peso=800
  
  def funciones(self):
    self.enciente=True
    self.arranca= True
    self.acelera=True
    self.frena= True
  
  def datos(self):
    print(f'Marca del auto: {self.marca}\nPuertas: {self.puertas}\nColor: {self.color}\nPeso: {self.peso}kg')

miAuto=Auto()
miAuto.datos()