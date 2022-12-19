miArchivo=open('Archivo.txt','w') #con la 'w' le indico que vamosa escribir en el archivo, y si no existe, lo va a crear

texto='''Esta aprendiendo a generar archivos de texto
con python, utilizando la 
herramienta VSC'''
miArchivo.write(texto)
miArchivo.close()

""" miArchivo=open('Archivo.txt','r') #'r' indica que vamos a leer el archivo
texto=miArchivo.read()
miArchivo.close()

print(texto) """

#ver el texto en modo de lista, cada linea en un arreglo
miArchivo=open('Archivo.txt','r') #'r' indica que vamos a leer el archivo
texto=miArchivo.readlines()
miArchivo.close()

print(texto)
print(texto[1])
