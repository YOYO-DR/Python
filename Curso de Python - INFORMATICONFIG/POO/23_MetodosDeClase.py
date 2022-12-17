class Operaciones:
  def __init__(self):
    self.valor1=int(input('Ingrese el primer valor: '))
    self.valor2=int(input('Ingrese el segundo valor: '))
    self.sumar()
    self.restar()
    self.multiplicar()

  def sumar(self):
    suma=self.valor1+self.valor2
    print(f'La suma es {suma}')
  
  def restar(self):
    resta=self.valor1-self.valor2
    print(f'La diferencia es {resta}')
  
  def multiplicar(self):
    multiplica=self.valor1*self.valor2
    print(f'El producto es {multiplica}')


resultado=Operaciones()