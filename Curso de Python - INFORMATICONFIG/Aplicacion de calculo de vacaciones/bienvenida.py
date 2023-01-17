from tkinter import *
import os
from tkinter import messagebox
from Licencia import Licencia

class Bienvenida:
  def __init__(self):
    #Creo la ventana
    self.ventana=Tk()

    #le agrego un titulo a la ventana
    self.ventana.title('Acceso')
    #configuro de que no se pueda modificar el tamaño
    self.ventana.resizable(False,False)

    #configuro el tamaño de la ventana, y la posicion donde quiero que aparezca inicialmente
    self.ventana.geometry('350x450+1000+50')

    #configuro el color de la ventana
    self.ventana.configure(bg='red')

    #configuro carpeta de imagenes
    self.carpetaImagenes=os.path.join(os.path.dirname(__file__),'imagenes')

    #abro la imagen
    self.fondo=PhotoImage(file=(os.path.join(self.carpetaImagenes,'logo-coca.png')))

    #creo label donde va la imagen
    Label(self.ventana,image=self.fondo,bg='red').pack()

    #configurar icono
    self.ventana.iconbitmap(os.path.join(self.carpetaImagenes,'icon0.ico'))

    #-------------------------------Labels-------------------------------#
    self.label1=Label(self.ventana,text='Sistema de control vacacional')
    self.label1.config(fg='White',bg='red',font=('andale mono regular',18,'italic'))
    self.label1.place(x=10,y=140)

    self.label2=Label(self.ventana, text='Ingrese su nombre')
    self.label2.config(fg='white',bg='red',font=('andale mono regular',12,'bold'))
    self.label2.place(x=50,y=230)

    self.label3=Label(self.ventana, text='©2022 The Coca-Cola Company.')
    self.label3.config(bg='red',fg='white',font=('andale mono regular',10,'bold'))
    self.label3.place(x=70,y=410)

    #Entry nombre de usuario
    self.dato1=StringVar()
    self.entry1=Entry(self.ventana, bd=2, bg='#eee8e8',fg='red',textvariable=self.dato1)
    self.entry1.config(font=('andale mono regular',12,'bold'), width=27)
    self.entry1.place(x=50,y=255)

    #boton de login
    self.boton1=Button(self.ventana, text='Ingresar', bd=2,bg='white',fg='red',command=self.acceso)
    self.boton1.config(font=('andale mono regular',14), width=12)
    self.boton1.place(x=100,y=285)

    self.ventana.mainloop()
  
  def acceso(self):
    self.largo=self.dato1.get()
    if not self.dato1.get():
      messagebox.showerror('ATENCION','Debe colocar nombre de usuario')
    elif len(self.largo)>0 and len(self.largo)<8:
      messagebox.showerror('ATENCION','El nombre de usuario debe tener más de 8 caracteres')
    else:
      self.ventana.destroy()
      Licencia()

if __name__ == '__main__':
  ejecutar=Bienvenida()
