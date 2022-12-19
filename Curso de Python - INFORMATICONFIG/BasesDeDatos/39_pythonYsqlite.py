import sqlite3

conexion=sqlite3.connect('Base1')

cursor=conexion.cursor()

#cursor.execute('''create table usuarios(
#                  nombre varchar(20),
#                  edad int,
#                  direccion varchar(50),
#                  telefono numeric(10)
#)''')

#cursor.execute('''insert into usuarios values('Jose',33,'calle primera No.50',123456789)''')
masUsuarios=[
  ('pedro',34,'calle 2da No 55',543534534),
  ('Yoiner',39,'calle 5da No 50',654645645),
  ('Tomas',29,'calle 3da No 65',56465645654)
  ]

cursor.executemany('insert into usuarios values(?,?,?,?)',masUsuarios)

conexion.commit()

conexion.close()