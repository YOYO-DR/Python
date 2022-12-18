from tkinter import *
import os
ventana=Tk()
ventana.geometry('400x500')
label1=Label(ventana, text='Indique su lenguaje de programacion favorito',font=('arial',14))
label1.place(x=10,y=20)

label2=Label(ventana,font=('arial',16))
label2.place(x=10,y=360)

def lenguajes():
  if seleccion.get()==1:
    label2.config(text='Seleccionaste Python')
  elif seleccion.get()==2:
    label2.config(text='Seleccionaste Java')
  elif seleccion.get()==3:
    label2.config(text='Seleccionaste C#')

seleccion=IntVar()
seleccion.set(3)

carpetaMedia=os.path.join(os.path.dirname(__file__),'media')

imgPython=PhotoImage(file=os.path.join(carpetaMedia,'python.png')).subsample(8)
imgJava=PhotoImage(file=os.path.join(carpetaMedia,'java.png')).subsample(15)
imgJs=PhotoImage(file=os.path.join(carpetaMedia,'js.png')).subsample(4)



radio1=Radiobutton(ventana,text='Python',variable=seleccion,value=1,command=lenguajes,image=imgPython)
radio1.place(x=10,y=60)

radio2=Radiobutton(ventana,text='Java',variable=seleccion,value=2,command=lenguajes,image=imgJava)
radio2.place(x=10,y=140)

radio3=Radiobutton(ventana,text='JavaScript',variable=seleccion,value=3,command=lenguajes,image=imgJs)
radio3.place(x=10,y=280)

ventana.mainloop()