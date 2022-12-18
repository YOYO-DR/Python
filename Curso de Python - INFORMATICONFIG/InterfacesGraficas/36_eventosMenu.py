from tkinter import *
from tkinter import messagebox

ventana=Tk()
ventana.geometry('500x500+850+35')

def acercaDe():
  messagebox.showinfo('Mi software','Sistema de procesos informaticos')

def actualiza():
  messagebox.showwarning('Actualización','''Actualización disponible
  debe actualizar el sistema
  visite: www.misistema.com''')

def salir():
  seleccion=messagebox.askokcancel('Salir','¿Desea salir de la aplicacion?')
  if seleccion==True:
    ventana.destroy()

def cierraDoc():
  seleccion=messagebox.askretrycancel('Reintenar','Error en cierre de archivo')
  if seleccion==False:
    ventana.destroy()
#creo la barra y la relaciono con la ventana
barraMenu=Menu(ventana)

#configuro la ventana,indicandole el menu creado y un tamaño
ventana.config(menu=barraMenu,width=600,height=400)

#esto nos va a permitir desplegar las opciones de ese menu que creamos
#tearoff=0 es para que no aparezca esa primer linea de opcion
menuArchivo=Menu(barraMenu,tearoff=0)
menuArchivo.add_command(label='Nuevo')
menuArchivo.add_command(label='Abrir')
menuArchivo.add_command(label='Guardar')
menuArchivo.add_command(label='Guardar como...')
menuArchivo.add_separator() # linea para agrupar
menuArchivo.add_command(label='Cerrar',command=cierraDoc)
menuArchivo.add_command(label='Cerrar todo')
menuArchivo.add_command(label='Salir',command=salir)

#agrego una opcion tipo cascade y con label, le indico el nombre
#luego en menu, le indico la variable donde tengo las opciones
barraMenu.add_cascade(label='Archivo',menu=menuArchivo)


#menu edit
menuEdit=Menu(barraMenu,tearoff=0)
menuEdit.add_command(label='Cortar')
menuEdit.add_command(label='Pegar')
menuEdit.add_command(label='Imprimir')

barraMenu.add_cascade(label='Edición',menu=menuEdit)

#menu Ayuda

menuAyuda=Menu(barraMenu,tearoff=0)
menuAyuda.add_command(label='Soporte')
menuAyuda.add_command(label='Actualizaciones',command=actualiza)
menuAyuda.add_command(label='Acerca de...',command=acercaDe)

barraMenu.add_cascade(label='Ayuda',menu=menuAyuda)

#cambiar tipo de letra de las opciones
ventana.option_add('*font','verdana 12')

ventana.mainloop()