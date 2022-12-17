#metodo constructor

class Persona:
  pass
  def __init__(self,nombre,año):
    self.nombre=nombre
    self.año=año

  def descripcion(self):
    return f'{self.nombre} tiene {self.año} años'

  def comentario(self,frase):
    return f'{self.nombre} dice: {frase}'

doctor=Persona('Jose', 26)
#print(doctor.nombre)
#print(doctor.descripcion())
#print(doctor.comentario('Hola, que tal bro'))

#modificar un atributo

class Email:
  pass
  def __init__(self):
    self.enviado=False

  def enviarCorreo(self):
    self.enviado=True

miCorreo=Email()
print(miCorreo.enviado)
miCorreo.enviarCorreo()
print(miCorreo.enviado)
