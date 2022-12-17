class Cajero:
  monto=50000
  print(f'BIENVENIDO A SU CAJERO AUTOMATICO')
  def operaciones(self):
    self.opcion=int(input('''
    -------------------------------------------------
    POR FAVOR INDIQUE QUE OPERACION DESEA REALIZAR...
    1. CONSULTAR BALANCE
    2. DEPOSITO A CUENTA
    3. RETIRO DE EFECTIVO
    4. SALIR
    ELIGE: '''))
    self.control=0
    while self.control==0:
      if self.opcion==1:
        self.consultaBalance()
      elif self.opcion==2:
        self.depositar()
      elif self.opcion==3:
        self.retirar()
      elif self.opcion==4:
        self.control=1
        self.salir()
      else:
        print('Opcion '+str(self.opcion)+' no valida, intente de nuevo')
        self.operaciones()
  def consultaBalance(self):
    print(f'Su balance disponible es: {self.monto}')
    print('¿Desea realizar otra operacion?')
    self.operaciones()

  def depositar(self):
    self.deposito=int(input('Indique la cantidad a depositar: '))
    self.monto+=self.deposito
    self.consultaBalance()

  def retirar(self):
    self.retiro=int(input('Indique la cantidad a retirar: '))
    self.control=0
    while self.control==0:
      if self.retiro>self.monto:
        print('''Usted no posee fondos suficientes para este retiro
        Por favor intente de nuevo
        -----------------------------------------------------------''')
        self.retiro=int(input('Indique la cantidad a retirar: '))
      elif self.retiro<=self.monto:
        self.monto-=self.retiro
        self.control=0
        print(f'Cantidad retirada: {self.retiro}')
        self.consultaBalance()

  def salir(self):
    print('------------------------------------------------------------\nGRACIAS POR USAR NUESTROS SERVICIOS\n------------------------------------------------------------')

ejecucion=Cajero()
ejecucion.operaciones()