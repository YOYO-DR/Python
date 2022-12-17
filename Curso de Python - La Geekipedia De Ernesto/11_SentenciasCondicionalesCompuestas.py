'''
numUno=5
if numUno==5:
    print("El número es cinco.")
else:
    print("El número NO es cinco")

print("Fin.")
'''
print("Sistema para calcular el promedio de un alumno.")

nombre=input("Para comenzar, ¿Cúal es tu nombre?: ")
mate=float(input(nombre+" ¿Cúal es tu calificacion en matematicas?:  "))
quimi=float(input(nombre+" ¿Cúal es tu calificacion en quimica?:  "))
bio=float(input(nombre+" ¿Cúal es tu calificacion en biologia?:  "))

prom=(mate+quimi+bio)/3

if prom>=6:
    
    print('Felicidades '+nombre+' "Aprobaste" con un promedio de:',prom)
    print('Felicidades '+nombre+' "Aprobaste" con un promedio de: ',round(prom,2))
else:
    print("Lo sentimos "+nombre+" has 'Reprobado' con un promedio de: ",prom)
    print("Lo sentimos "+nombre+" has 'Reprobado' con un promedio de: ",round(prom,1))
print("Fin.")
