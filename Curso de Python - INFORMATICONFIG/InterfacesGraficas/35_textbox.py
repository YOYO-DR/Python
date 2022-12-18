from tkinter import *
import os

ventana=Tk()
ventana.geometry('550x550')

labelComent=Label(ventana,text='Comentarios',font=('arial',14))

#posicionamos por medio de grid() que funciona por medio de columnas y filas
labelComent.grid(row=0,column=0) 

#Creamos la caja de texto
textComent=Text(ventana,font=('consolas',16))

#Posicionamos con grid
#padx y pady configuramos el padding de la caja de texto
textComent.grid(row=1,column=0,padx=20,pady=15)

#configuramos el tamaño de la caja
textComent.config(width=30,height=10)

#configurar scrooll vertical
#creo el objeto Scrollbar, en command le indico la caja de texto y con yview que va a ser el scrol vertical
scrollVertical=Scrollbar(ventana,command=textComent.yview)

#lo posiciono con grid y con sticky='nsew' le digo que se alargue a toda la caja
scrollVertical.grid(row=1,column=1,sticky='nsew') 

#con esta configuracion, le digo al scrooll que siga al texto
textComent.config(yscrollcommand=scrollVertical.set)



ventana.mainloop()