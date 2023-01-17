from tkinter import *
import os
from tkinter import ttk,messagebox
import sys

class Principal:
  def __init__(self):
    self.ventana=Tk()
    self.ventana.title('Pantalla principal')
    self.ventana.resizable(False,False)
    self.ventana.geometry('640x535+711+127')
    self.ventana.config(bg='red')
    #carpeta imagenes
    self.carpetaImagenes=os.path.join(os.path.dirname(__file__),'imagenes')
    self.ventana.iconbitmap(os.path.join(self.carpetaImagenes,'icon0.ico'))

    #menu de opciones
    self.menuBar1=Menu(self.ventana)
    self.ventana.config(menu=self.menuBar1)

    self.opciones1=Menu(self.menuBar1,tearoff=0)
    self.opciones2=Menu(self.menuBar1,tearoff=0)

    self.menuBar1.add_cascade(label='Opciones',menu=self.opciones1)
    self.opciones1.add_command(label='Salir',font=('Arial',10,'bold'),command=self.salir)

    self.menuBar1.add_cascade(label='Acerca de',menu=self.opciones2)
    self.opciones2.add_command(label='Info',font=('Arial',10,'bold'),command=self.acerca)

    #imagen logo
    self.fondo=PhotoImage(file=os.path.join(self.carpetaImagenes,'coca-cola-p.png'))
    Label(self.ventana,image=self.fondo,bg='red').place(x=0,y=0)

    #Label bienvenida
    self.l_bienvenida=Label(self.ventana,text='Bienvenid@!')
    self.l_bienvenida.config(fg='white',bg='red',font=('andale mono regular',20,'bold'))
    self.l_bienvenida.place(x=340,y=30)

    #label detalle
    self.l_detalle=Label(self.ventana,text='Datos del trabajador para el calculo de vacaciones')
    self.l_detalle.config(fg='white',bg='red',font=('andale mono regular',18,'bold'))
    self.l_detalle.place(x=30,y=110)

    #label nombre completo
    self.l_nombre=Label(self.ventana,text='Nombre completo')
    self.l_nombre.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
    self.l_nombre.place(x=30,y=160)

    self.datoNombre=StringVar()
    self.e_nombre=Entry(self.ventana,bd=2,bg='#eee8e8',fg='red',textvariable=self.datoNombre)
    self.e_nombre.config(font=('andale mono regular',12,'bold'), width=22)
    self.e_nombre.place(x=30,y=185)

    #label apellido paterno
    self.l_paterno=Label(self.ventana,text='Apellido paterno')
    self.l_paterno.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
    self.l_paterno.place(x=30,y=225)

    self.datoApa=StringVar()
    self.e_apaterno=Entry(self.ventana,bd=2,bg='#eee8e8',fg='red',textvariable=self.datoApa)
    self.e_apaterno.config(font=('andale mono regular',12,'bold'), width=22)
    self.e_apaterno.place(x=30,y=250)

    #label apellido materno
    self.l_materno=Label(self.ventana,text='Apellido materno')
    self.l_materno.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
    self.l_materno.place(x=30,y=295)

    self.datoAma=StringVar()
    self.e_amaterno=Entry(self.ventana,bd=2,bg='#eee8e8',fg='red',textvariable=self.datoAma)
    self.e_amaterno.config(font=('andale mono regular',12,'bold'), width=22)
    self.e_amaterno.place(x=30,y=320)

    #select departamento
    self.l_departamento=Label(self.ventana,text='Seleccione departamento')
    self.l_departamento.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
    self.l_departamento.place(x=310,y=160)

    self.var_combo1=StringVar()
    self.op_combo=('','Atencion al cliente','Departamento de logistica','Departamento de gerencia')
    self.combobox1=ttk.Combobox(self.ventana,state='readonly',
                                width=20,font=('andale mono regular',11,'bold'),
                                textvariable=self.var_combo1,values=self.op_combo)
    self.combobox1.current(0) #para que no tenga un valor al inicio
    self.combobox1.place(x=310,y=185)

    #select antiguedad
    self.l_antiguedad=Label(self.ventana,text='Seleccione antiguedad')
    self.l_antiguedad.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
    self.l_antiguedad.place(x=310,y=225)

    self.var_combo2=StringVar()
    self.op_combo2=('','1 anio de servicio','2 a 6 anios de servicio','7 o mas anios')
    self.combobox2=ttk.Combobox(self.ventana,state='readonly',
                                width=20,font=('andale mono regular',11,'bold'),
                                textvariable=self.var_combo2,values=self.op_combo2)
    self.combobox2.current(0) #para que no tenga un valor al inicio
    self.combobox2.place(x=310,y=250)

    #variable para estilo de los combobox
    estilo=ttk.Style()
    estilo.theme_use('clam')
    estilo.configure("TCombobox",background="red")
    #-------------------------------------

    #label resultado
    self.l_resultado=Label(self.ventana, text='Resultado del calculo')
    self.l_resultado.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
    self.l_resultado.place(x=310,y=295)

    self.area_resultado=Text(self.ventana,width=35,height=7)
    self.area_resultado.config(font=('andale mono regular',11,'bold'),bg='#eee8e8',fg='red',state=DISABLED)
    self.area_resultado.place(x=310,y=320)

    #label pie de interfaz
    self.l_footer=Label(self.ventana, text='©2022 The Coca-Cola Company.')
    self.l_footer.config(fg='white',bg='red',font=('andale mono regular',10,'bold'))
    self.l_footer.place(x=205,y=480)

    #botones
    self.b_calcular=Button(self.ventana,text='Calcular', width=8,height=2,command=self.controlDatos)
    self.b_calcular.config(font=('andale mono regular',12,'bold'),fg='white',bg='red',bd=5)
    self.b_calcular.place(x=130,y=365)

    self.b_limpiar=Button(self.ventana,text='Limpiar', width=8,height=2,command=self.limpiaDatos)
    self.b_limpiar.config(font=('andale mono regular',12,'bold'),fg='white',bg='red',bd=5)
    self.b_limpiar.place(x=30,y=365)

    self.ventana.mainloop()
  
  def controlDatos(self):
    if not self.datoNombre.get() or not self.datoApa.get() or not self.datoAma.get() or self.var_combo1.get()=='' or self.var_combo2.get()=='':
      messagebox.showerror('AVISO','No deben quedar campos vacios.')
    if len(self.datoNombre.get())>12 or len(self.datoApa.get())>15 or len(self.datoAma.get())>15:
      messagebox.showerror('AVISO','Nombre / Apellido(s) muy largos.')
    else:
      self.area_resultado.config(state=NORMAL)
      self.area_resultado.delete('1.0',"end")
      if self.var_combo1.get()=='Atencion al cliente':
        if self.var_combo2.get()=='1 anio de servicio':
          self.area_resultado.insert(INSERT,self.datoNombre.get()+' '+self.datoApa.get()+' '+self.datoAma.get()+\
                                    '\nDepartamento: '+self.var_combo1.get()+\
                                    '\nAntiguedad: '+self.var_combo2.get()+\
                                    '\n\nRecibe 14 dias de vacaciones')
        if self.var_combo2.get() == '2 a 6 anios de servicio':
                    self.area_resultado.insert(INSERT, self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')
        if self.var_combo2.get() == '7 o mas anios':
                    self.area_resultado.insert(INSERT, self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 22 DIAS DE VACACIONES')
      if self.var_combo1.get() == 'Departamento de logistica':
        if self.var_combo2.get() == '1 anio de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 10 DIAS DE VACACIONES')
        if self.var_combo2.get() == '2 a 6 anios de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 15 DIAS DE VACACIONES')
        if self.var_combo2.get() == '7 o mas anios':
                    self.area_resultado.insert(INSERT,
                                               self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 20 DIAS DE VACACIONES')
      if self.var_combo1.get() == 'Departamento de gerencia':
        if self.var_combo2.get() == '1 anio de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')
        if self.var_combo2.get() == '2 a 6 anios de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 25 DIAS DE VACACIONES')
        if self.var_combo2.get() == '7 o mas anios':
                    self.area_resultado.insert(INSERT,
                                               self.datoNombre.get() + ' ' + self.datoApa.get() + ' ' + self.datoAma.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 30 DIAS DE VACACIONES')
      self.area_resultado.config(state=DISABLED)

  def limpiaDatos(self):
    self.area_resultado.config(state=NORMAL)
    self.area_resultado.delete('1.0','end')
    self.area_resultado.config(state=DISABLED)
    self.e_nombre.delete('0','end')
    self.e_apaterno.delete('0','end')
    self.e_amaterno.delete('0','end')
    self.combobox1.current(0)
    self.combobox2.current(0)

  def acerca(self):
    messagebox.showinfo('Info','''    SISTEMA DE CONTROL DE VACACIONES
    Desarrollado por: YOYODR EL MEJOR©
    Derechos reservados 2022''')
  
  def salir(self):
    sys.exit()



