class Software:
  def __init__(self):
    self.sistemaOperativo=input('Indique el sistema operativo: ')
    self.arquitectura=int(input('Ingrese arquitectura (32/64):'))
  
  def info(self):
    print(f'Sistema Operativo: {self.sistemaOperativo}')
    print(f'Arquitectura: {self.arquitectura}')

class Base(Software):
  def __init__(self):
    super().__init__()
    self.procesador=input('Indique procesador: ')
    print('____________________________________')
  
  def imprime(self):
    print(f'Procesador: {self.procesador}')

pc1=Base()

pc1.info()

pc1.imprime()