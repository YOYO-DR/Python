from tkinter import *
import sys

ventana=Tk()
ventana.geometry("500x500")
labelMensaje=Label(ventana, text='¿Desea mostrar saludo?',font=('verdana',18))
labelMensaje.place(x=10,y=20)

def saludo():
  labelMensaje.config(text='Hola a todos')

botonAceptar=Button(ventana, text='Aceptar',command=saludo,bg='green',fg='white')
botonAceptar.config(width=10, height=3)
botonAceptar.place(x=10,y=70)

def cancelar():
  sys.exit()

botonCancelar=Button(ventana, text='Cancelar',command=cancelar)
botonCancelar.config(width=10, height=3)
botonCancelar.place(x=110,y=70)
ventana.mainloop()