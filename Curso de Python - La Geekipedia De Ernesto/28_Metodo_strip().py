""" cadena=" Hola yoiner "
print(cadena)
cadena=cadena.strip()
print(cadena) """
#cadena='\tHola Ernesto\n'
#print(cadena)
#cadena = cadena.strip('s tHo')
##No aplica nada, porque un ' ' no es un \t o \n, solo aplica con el strip() vacio
#print(cadena)
#
#cadena='alexander'
#print(cadena)
#cadena = cadena.strip('a hdner')
#print(cadena)

################################################################

nombre=input('Dame tu nombre: ')
print(nombre)
cortar=input('Que parte va a cortar: ')
posicion=[nombre.index(cortar),len(cortar)]
nombre=list(nombre)
sub=nombre

for i in range(posicion[1]):
  del sub[posicion[0]]

valorRecortado=''

for i in sub:
  valorRecortado+=i
print(f"\n{valorRecortado}")


