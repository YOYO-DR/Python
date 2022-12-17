from tkinter import *
import os
ventana=Tk()
ventana.geometry("500x300")
ventana.config(bg='yellow')
ventana.title('VENTANA PRINCIPAL')
ventana.resizable(width=False,height=False)

#Como configurar la carpeta de imagenes u otra carpeta
#importat libreria 'os'
carpetaPrincipal=os.path.dirname(__file__) 
#aqui configuro cual es la carpeta principal, con '__file__' le digo que va a ser la carpeta donde esta todo lo que voy a utilizar, la carpeta principal

carpetaMedia=os.path.join(carpetaPrincipal, 'media') 
#aqui configuro cual es la carpeta donde van las imagenes (media),parandole la carpeta principal y luego el nombre de la carpeta a indicar (media)
ventana.iconbitmap(os.path.join(carpetaMedia, 'python.ico')) #en la funcion 'iconbitmap' le paso como parametro 'os.path.join()' y a esa funcion, le paso la variable donde esta la ruta de la carpeta a utilizar, y como segundo parametro, nombre del archivo

ventana.mainloop()