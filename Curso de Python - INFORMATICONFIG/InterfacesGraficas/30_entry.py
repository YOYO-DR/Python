from tkinter import *

ventana=Tk()

ventana.geometry("300x500")

nombreLabel=Label(ventana, text='Ingrese nombre', font=('arial',16)).place(x=10, y=55)

campoNombre=Entry(ventana, bg='yellow',bd=8,cursor='arrow',font=('consolas',14),fg='brown')
campoNombre.place(x=10,y=90)#,width=90,height=40)

claveLabel=Label(ventana, text='Ingrese contraseña', font=('arial',16)).place(x=10, y=140)
campoClave=Entry(ventana,show='*',bg='yellow',bd=8,cursor='arrow',font=('consolas',14),fg='brown')
campoClave.place(x=10,y=175)



ventana.mainloop()