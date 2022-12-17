'''numUno=5
if numUno==5:
    print("El número es cinco")
print("Fin.")
'''
print("Sistema para calcular el promedio de un alumno.")

nombre=input("Para comenzar, ¿Cúal es tu nombre?: ")
mate=int(input(nombre+" ¿Cúal es tu calificacion en matematicas?:  "))
quimi=int(input(nombre+" ¿Cúal es tu calificacion en quimica?:  "))
bio=int(input(nombre+" ¿Cúal es tu calificacion en biologia?:  "))

prom=(mate+quimi+bio)/3
prom=int(prom)
if prom>=6:
    
    print('Felicidades '+nombre+' "Aprobaste" con un promedio de: ',prom)

print("Fin.")