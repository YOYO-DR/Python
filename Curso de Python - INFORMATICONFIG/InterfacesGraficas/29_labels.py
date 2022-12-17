from tkinter import *
import os
ventana=Tk()
ventana.geometry('300x400')
etiqueta=Label(ventana,text='Linea de texto',fg='green',font=('verdana',18))
etiqueta.place(x=100,y=200)

carpetaMedia=os.path.join(os.path.dirname(__file__),'media')
#objeto tipo imagen
deku=PhotoImage(file=os.path.join(carpetaMedia,'deku.png')) #configurar ruta

Label(ventana,image=deku).place(x=10,y=0) #crear Label, poner imagen y su posicion
ventana.mainloop()