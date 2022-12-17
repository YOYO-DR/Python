#herencia
class Pokemon:
  pass
  def __init__(self,nombre,tipo):
    self.nombre=nombre
    self.tipo=tipo
  
  def descripcion(self):
    return f"{self.nombre} es un Pokemon de tipo: {self.tipo}"

class Pikachu(Pokemon):
  def ataque(self,tipoAtaque):
    return f"{self.nombre} tipo de ataque: {tipoAtaque}"

class Charmander(Pokemon):
  def ataque(self,tipoAtaque):
    return f"{self.nombre} tipo de ataque: {tipoAtaque}"

nuevoPokemon=Pikachu('boby','electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('Impacto trueno'))

