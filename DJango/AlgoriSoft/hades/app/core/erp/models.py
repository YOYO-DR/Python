from django.db import models
from datetime import datetime

class Empleado(models.Model):
  names=models.CharField(max_length=150,verbose_name='Nombres',default='Sin nombres')
  #names=models.TextField()
  #diferencia entre CharField y TExtField es que al charfield toca especificarle el maximo de caracteres, al textfield no
  #verbose_name es como un alias cuando se vaya a mostrar

  dni=models.CharField(max_length=10,unique=True,verbose_name='Dni') #unique= es para que sea unico
  date_joined=models.DateField(default=datetime.now,verbose_name='Fecha de registro')
  #DateField es para fechas
  #default es para poner un valor por defecto si no se ingresa alguno

  date_creation=models.DateTimeField(auto_now=True)#auto_now es para que se ingrese la fecha actual del registro y no se modifique mas
  date_update=models.DateTimeField(auto_now_add=True)#auto_now_add es para que cada vez que se ingrese un registro, se modifique con la fecha actual
  age=models.PositiveIntegerField(default=0) 
  #IntegerField valores enteros
  #PositiveIntegerField valores enteros positivos (y contrario con Negative)
  salary=models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
  #max_digits para un maximo de digitos
  #decimal_places para un el maximo de decimales 
  estate=models.BooleanField(default=True) #para valores booleanos
  avatar=models.ImageField(upload_to='avatar/%Y/%m/%d')#para imagenes, en upload_to le especifico la carpeta donde se guarde, el nombre y los "/" es que le digo que se guarde en modo de fecha en ese modo (y/m/d)


