import sqlite3

conexion = sqlite3.connect('datosg50.db')

try:
    conexion.execute('''
                create table articulo(
                    codigo integer primary key autoincrement,
                    detalle text,
                    precio real
                )
    ''')
    
    print("tabla creada....")
except sqlite3.OperationalError:
    print("la tabla ya existe")
    
conexion.close()