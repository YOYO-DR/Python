""" nombre='CarloS gallardo'
print(nombre.title()) #Muestra el formato que aplica .title pero no afecta la variable
print(nombre) """
#Si quiero modificar
""" nombre='CarloS gallardo'
print(nombre.istitle()) #verifica que la variable este en el formato esperado - retorna false o true
nombre=nombre.title()
print(nombre) """

#Ejemplo
first_name=input('Nombre: ')
last_name=input('Apellido: ')
full_name=f'{first_name} {last_name}'
print()
print(f'¿El formato del método title() se ha aplicado?: {full_name.istitle()}')
print(f'Aplicando el métdo title(): {full_name.title()}')
print(f'Volvemos a imprimir el nombre: {full_name}')
print()
full_name=full_name.title()
print(f'¿El formato del método title() se ha aplicado?: {full_name.istitle()}')