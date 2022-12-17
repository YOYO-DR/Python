print("=========")
print("Conversor")
print("=========\n")
print("Menú de opciones:\n")
print("Presiona 1 para convertir de número a palabra")
print("Presiona 2 para convertir de palabra a número\n")
opcion=int(input("¿Cúal es tu opción deseada?: "))
if opcion==1:
    print("\nConversor de número a palabra\n")
    opcion=int(input("¿Cúal es el número que seas convertir a palabra?: "))
    if opcion==1:
        print("El número es 'Uno'")
    elif opcion==2:
        print("El número es 'Dos'")
    elif opcion==3:
        print("El número es 'Tres'")
    elif opcion==4:
        print("El número es 'Cuatro'")
    else:
        print("La opcion no esta registrada")
        
elif opcion==2:
    print("Conversor de palabra a número")
    opcion=input("¿Cúal es la palabra que seas convertir a número?: ")
    opcion=opcion.lower()
    if opcion=="uno":
        print("El número es '1'")
    elif opcion=="dos":
        print("El número es '2'")
    elif opcion=="tres":
        print("El número es '3'")
    elif opcion=="cuatro":
        print("El número es '4'")
    else:
        print("La opcion no esta registrada")
else:
    print("La opcion no existe")
print("Fin.")