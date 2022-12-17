""" listaEnteros=[1,2,3,4,5]
#print(listaEnteros)
listaLetras=['a', 'b', 'c', 'd']
#print(listaLetras)
materias=['Fisica', 'matematicas','1990',True]
#print(materias)
precios=[50.26,10.3,100.5,40.1]
#print(precios)

#print(listaEnteros[2])
#print(listaLetras[1:5])
#print(materias[:3])
#print(precios[2:])

 listaLetras.append('e')
print(listaLetras)
materias.append('Biologia')
print(materias) 

 del listaLetras[2]
print(listaLetras)
del precios[3]
print(precios) """

#print([1,2,3] + [4,5,6])
#print(4 in [1,2,3])

#Video 16 - Listas (parte 2)
listaEnteros=[1,2,3,4,5,5,5,5]
listaLetras=['a', 'b', 'c', 'd']
materias=['Fisica', 'matematicas','1990',True]
precios=[50.26,10.3,100.5,40.1]

#print(len(listaEnteros))
#print(max(precios))
#print(min(precios))
#print(listaEnteros.count(5))

#materias.extend('1990')
#print(materias)
#precios.pop(2)
#print(precios)
#listaEnteros.remove(2)
#print(listaEnteros)

listaLetras.reverse()
#print(listaLetras)

for i in materias:
  print(i,end=' / ')
print()
