#f-strings
#format %

#curso='python'
#print('tutoriales de %s'%curso)

#nombre='victor'
#edad=25
#print('hola, soy %s y tengo %s años.'%(nombre,edad))

#str.format()

#nombre='victor'
#edad=25

#print('\nQue tal, soy {} y mi edad es {} años'.format(nombre,edad))
#print(f'hola, soy {nombre} y mi edad es {edad} años.')

#f-strings

class Estudiante:
  def __init__(self,nombre,apellido,edad):
    self.nombre=nombre
    self.apellido=apellido
    self.edad=edad

  def __repr__(self):# este si se va a ejecutar apenas se llame al objeto, es la representacion oficial
    return f'\nHola que tal, soy {self.nombre} {self.apellido}, {self.edad} años.'

#  def __str__(self):
#    return f'Hola que tal, soy {self.nombre} {self.apellido}, {self.edad} años.' # con __str__ es como acomodo la informacion del objeto, y solo es llamar al objeto en un print, o sin print nomas seria poner el print en el __str__

nuevoEstudiante=Estudiante('victor','cruz',17)
print(f'{nuevoEstudiante !r}')#asi entiende el valor de cada variable
