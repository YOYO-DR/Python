#polimorfismo por funcion

"""class Tomate:
  def tipo(self):
    print('vegetal')
  def color(self):
    print('rojo')

class Manzana:
  def tipo(self):
    print('fruta')
  def color(self):
    print('verde')

def funcion(objeto):
  objeto.tipo()
  objeto.color()

nuevoTomate=Tomate()
funcion(nuevoTomate)

nuevaManzana=Manzana()
funcion(nuevaManzana)
"""
#polimorfismo con metodos
""" 
class Colombia:
  def capital(self):
    print('Bogota')
  def idioma(self):
    print('Español')

class Francia:
  def capital(self):
    print('Paris')
  def idioma(self):
    print('Frances')

print()
colombiano=Colombia()
frances=Francia()
for pais in (colombiano, frances):
  pais.capital()
  pais.idioma()
  print()
print()
 """
#polimorfismo con herencia

class Aves:
  def volar(self):
    print('La mayoria de las aves pueden volar pero algunas no')

class Aguila(Aves):
  def volar(self):
    print('Las aguilas pueden volar')
class Gallinas(Aves):
  def volar(self):
    print('La gallina no puede volar')
print()

objAve=Aves()
objAguila=Aguila()
objGallina=Gallinas()
objAve.volar()
objAguila.volar()
objGallina.volar()

