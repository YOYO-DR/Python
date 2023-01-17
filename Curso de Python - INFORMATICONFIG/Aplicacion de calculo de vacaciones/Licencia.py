from tkinter import *
import os
from principal import Principal
import sys
class Licencia:
  def __init__(self):
    self.ventana=Tk()
    self.ventana.title('TERMINOS Y CONDICIONES')
    self.ventana.resizable(False,False)
    self.ventana.geometry('600x360+750+50')

    #Carpeta imagenes
    self.carpetaImagenes=os.path.join(os.path.dirname(__file__),'imagenes')

    #fondo
    self.fondo=PhotoImage(file=(os.path.join(self.carpetaImagenes,'coca-cola-l.png')))
    Label(self.ventana,image=self.fondo).place(x=300,y=220)

    #icono de la ventana
    self.ventana.iconbitmap(os.path.join(self.carpetaImagenes,'icon0.ico'))

    #-------------------------------labels-------------------------------#
    self.label1=Label(self.ventana,text='TERMINOS Y CONDICIONES')
    self.label1.config(font=('arial',13,'bold'))
    self.label1.place(x=180,y=10)

    self.textoCondiciones=Text(self.ventana,width=96,height=12)
    self.textoCondiciones.config(font=('arial',8),bg='white',state=NORMAL)
    self.textoCondiciones.insert(INSERT,'''       
    TÉRMINOS Y CONDICIONES"

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE INFORMATICONFIG.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  INFORMATICONFIG DE ERNESTO NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (INFORMATICONFIG), NO SE RESPONSABILIZA DEL USO QUE USTED"
    HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO)"
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE."
         ''')
    self.textoCondiciones.place(x=10,y=40)
    self.textoCondiciones.config(state=DISABLED)

    #checkbutton aceptar condiciones
    self.acepto=IntVar()
    self.checkAcepto=Checkbutton(self.ventana,text='Yo acepto',font=('arial',12,'bold'),command=self.aceptar)
    self.checkAcepto.place(x=10,y=260)

    #botones aceptrar y cancelar
    self.continuar=Button(self.ventana,text='Acepto',font=('arial',11,'bold'),\
                          width=7,height=2,bd=3,state=DISABLED,command=self.acceso)
    self.continuar.place(x=10,y=290)

    self.cancelar=Button(self.ventana,text='Cancelar',font=('arial',11,'bold'),\
                          width=7,height=2,bd=3,command=self.cancelar)
    self.cancelar.place(x=100,y=290)

    

    self.ventana.mainloop()
  
  def aceptar(self):
    if self.continuar['state']==DISABLED:
      self.continuar['state']=NORMAL
    else:
      self.continuar['state']=DISABLED
  
  def acceso(self):
    self.ventana.destroy()
    Principal()
  
  def cancelar(self):
    sys.exit()
