#herencia multiple
class Telefono:
  def __init__(self):
    pass
  def llamar(self):
    print('Llamando...')
  
  def ocupado(self):
    print('Ocupado...')


class Camara:
  def __init__(self):
    pass
  def fotografica(self):
    print('Tomando fotos...')

class Reproduccion:
  def __init__(self):
    pass
  def reproduccionDeMusica(self):
    print('Reproduciendo musica')
  def reproduccirVideo(self):
    print('Reproduccir un video')

class Smartphone(Telefono,Camara,Reproduccion):
  def __del__(self): #con esto destruyo esta clase, la destruye despues de utilizarla
    print('Telefono apagado')
  

movil=Smartphone()
#print(dir(movil)) #Con dir() veo las acciones o metodos que puede hacer ese objeto

movil.fotografica()
movil.llamar()