from tkinter import *
import os

ventana=Tk()
ventana.title('Menú') #titulo
ventana.geometry('400x600') #tamaño
ventana.resizable(width=False,height=False) #bloquear

carpetaMedia=os.path.join(os.path.dirname(__file__),'media')

imgMenu=PhotoImage(file=os.path.join(carpetaMedia,'combo.png')).subsample(4)

Label(ventana,image=imgMenu).place(x=100, y=5)
label1=Label(ventana,text='Elige tu combo',font=('arial',16)).place(x=130,y=190)

#esto recibe el valor entero del checkbuttons indicada,variable de captura de seleccion
hamburguesa=IntVar() 
papas=IntVar()
nuggets=IntVar()
soda=IntVar()
helado=IntVar()

def combo():
  opciones=''
  #con .get() obtenemos el valor de la variable de seleccion
  if hamburguesa.get()==1: 
    opciones+='Hamburguesa\n'
  if papas.get()==1:
    opciones+='Papas\n'
  if nuggets.get()==1:
    opciones+='Nuggets\n'
  if soda.get()==1:
    opciones+='Soda\n'
  if helado.get()==1:
    opciones+='Helado\n'
  if hamburguesa.get()==0 and papas.get()==0 and nuggets.get()==0 and soda.get()==0 and helado.get()==0:
    label2.config(text=f'No ha realizado su orden',font=('verdana',14))
    label2.place(x=80, y=390)
  else:
    label2.config(text=f'Su orden:\n{opciones}',font=('verdana',14))
    label2.place(x=130, y=390)

#creacion de chekbuttons
Checkbutton(ventana,text='Hamburguesa',font=('consolas',12),variable=hamburguesa,onvalue=1,offvalue=0,command=combo).place(x=10,y=220)
Checkbutton(ventana,text='Papas',font=('consolas',12),variable=papas,onvalue=1,offvalue=0,command=combo).place(x=10,y=250)
Checkbutton(ventana,text='Nuggets',font=('consolas',12),variable=nuggets,onvalue=1,offvalue=0,command=combo).place(x=10,y=280)
Checkbutton(ventana,text='Soda',font=('consolas',12),variable=soda,onvalue=1,offvalue=0,command=combo).place(x=10,y=310)
Checkbutton(ventana,text='Helado',font=('consolas',12),variable=helado,onvalue=1,offvalue=0,command=combo).place(x=10,y=340)

label2=Label(ventana)
label2.place(x=80, y=390)
label2.config(text=f'No ha realizado su orden',font=('verdana',14))


def pedirOrden():
  if hamburguesa.get()==0 and papas.get()==0 and nuggets.get()==0 and soda.get()==0 and helado.get()==0:
    label2.config(text=f'No has seleccionado ningun pedido',font=('verdana',14))
    label2.place(x=25, y=390)
  else:
    label2.config(text=f'¡Su pedido ha sido realizado!',font=('verdana',14))
    label2.place(x=60, y=390)



aceptar=Button(ventana,text='Pedir orden',command=pedirOrden,bg='green',font=('arial',12))
aceptar.place(x=85,y=550)
aceptar.config(width=10,height=1)

def reset():
  hamburguesa.set(0)
  papas.set(0)
  nuggets.set(0)
  soda.set(0)
  helado.set(0)
  label2.place(x=80, y=390)
  label2.config(text=f'No ha realizado su orden',font=('verdana',14))

reset=Button(ventana,text='Otro pedido',command=reset,bg='red',font=('arial',12))
reset.place(x=200,y=550)
reset.config(width=10,height=1)




ventana.mainloop()
