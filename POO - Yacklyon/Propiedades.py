#propiedades()

class Empleado:
  def __init__(self,nombre,salario):
    self.__nombre=nombre
    self.__salario=salario
  
  def __getnombre(self):
    return self.__nombre
  def __getsalario(self):
    return self.__salario

  def __setnombre(self,nombre):
    self.__nombre=nombre
  def __setsalario(self,salario):
    self.__salario=salario

  def __delnombre(self):
    del self.__nombre
  def __delsalario(self):
    del self.__salario

  nombre=property(fget=__getnombre,
  fset=__setnombre,
  fdel=__delnombre,
  doc='soy la propiedad del "nombre"')

  salario=property(fget=__getsalario)

empleadoUno=Empleado('Victor',3000)

empleadoUno.nombre='Sara'
print(empleadoUno.nombre,empleadoUno.salario)
help(empleadoUno)
""" empleado1=Empleado('Yoiner',2000)
print(f'{empleado1.getnombre()}, {empleado1.getsalario()}')
empleado1.setnombre('Raul')
print(f'{empleado1.getnombre()}, {empleado1.getsalario()}') """

