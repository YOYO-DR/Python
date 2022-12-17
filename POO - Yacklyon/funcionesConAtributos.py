#funciones para atributos

class Persona:
  edad = 27
  nombre = 'Victor'
  pais='Brazil'

doctor=Persona()
#print(f'La edad es: {doctor.edad}')
#print(f"La edad es: {getattr(doctor,'edad')}") #Lo utilizo para acceder al atributo por medio de este metodo

#print(f"¿el doctor tiene una edad?: {hasattr(doctor,'edad')}") #con este metodo pregunto si el Objeto tiene ese atributo

#print(f"¿el doctor tiene un apellido?: {hasattr(doctor,'apellido')}")

#print(f"antes era: {doctor.nombre}")
setattr(doctor, 'nombre','Hector') # con este metodo, llamo el objeto, le paso el nombre del atributo a modificar, y luego el valor nuevo

#tambien funciona para agregar un nuevo atributo

#print(f"Ahora se llama: {doctor.nombre}")

delattr(Persona,'pais') #con esto borro un atributo de esa clase

#print(f"¿el doctor tiene un pais?: {hasattr(doctor,'pais')}")
