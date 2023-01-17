import mysql.connector

try:
  conexion=mysql.connector.connect(
    host='20.168.252.60',
    user='yoyo',
    password='119351',
    port='3306',
    database='prueba2'
  )
  

except Exception as err:
  print("Error conectando a la base")
else:
  print('Conectado a Mysql\n')
try:
  cursor=conexion.cursor()
  insertar="insert into usuarios values(1002,'Miguel','123456')"
  cursor.execute(insertar)
  conexion.commit()
except Exception as err:
  print('Error insertando datos en la tabña',err)
else:
  print('Datos insertados correctamente')
conexion.close()