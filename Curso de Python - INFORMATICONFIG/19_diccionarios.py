paises={'Argentina':'Buenos Aires',
  'España':'Madrid',
  'Colombia':'Bogota',
  'Rep. Dominicana':'Santo domingos'}
#print(paises)

def dicPaises(paises):
  for capital in paises:
    print(capital,paises[capital])

#print(paises['Colombia'])
#dicPaises(paises)

def cargarProductos():
  productos={}
  for i in range(3):
    nombre=input('Ingrese nombre del producto: ')
    precio=int(input('Ingrese el precio: '))
    productos[nombre]=precio
  return productos

def imprime(productos):
  print('Listado de productos')
  for nombre in productos:
    print(nombre, productos[nombre])

articulos=cargarProductos()
imprime(articulos)