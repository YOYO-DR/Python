import random
adivinar=random.randint(1,10)
opcion=int(input('Ingresa un número entre 1 y 10: '))
while True:
  if opcion==adivinar:
    print(f'Excelente, el número a adivinar es ese! "{opcion}"')
    break
  elif opcion>adivinar:
    opcion=int(input(f'El número esta por debajo de {opcion}, vuelve a elegir: '))
  elif opcion<adivinar:
    opcion=int(input(f'El número esta por encima de {opcion}, vuelve a elegir: '))