print("\nSistema para medir dias de vacaciones de trabajadores\n")
nom=input("Igresa tu nombre: ")
clave=int(input("\nDame la clase de tu departamento (1,2,3):"))
anti=float(input("\nDame la antiguedad en la empresa en años:"))
dias=0

if clave==1:
  if anti>=1 and anti<2:
    dias=6
  elif anti>=2 and anti<7:
    dias=14
  else:
    dias=20
elif clave==2:
  if anti>=1 and anti<2:
    dias=7
  elif anti>=2 and anti<7:
    dias=15
  else:
    dias=22
elif clave==3:
  if anti>=1 and anti<2:
    dias=10
  elif anti>=2 and anti<7:
    dias=20
  else:
    dias=30

if clave<0 or clave>=4:
  print("\nEsa clave no existe")
else:
  if anti<=0:
    print(nom,"no tienes derecho a vacaciones")
  else:
    print(nom,"tienes derecho a",dias,"dias de vacaciones")