from tkinter import *
import os

ventana=Tk()


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
menuArchivo.add_command(label='Cerrar')

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
menuAyuda.add_command(label='Actualizaciones')
menuAyuda.add_command(label='Acerca de...')

barraMenu.add_cascade(label='Ayuda',menu=menuAyuda)



ventana.mainloop()