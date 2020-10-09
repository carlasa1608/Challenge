# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import leer_insumos

#Crear conexión y cursor
conexion = sqlite3.connect("base_datos")
cursor = conexion.cursor()

#Crear Tablas
#cursor.execute("CREATE TABLE info_usuarios (row_id INTEGER NOT NULL, user_id INTEGER NOT NULL, user_state TEXT,user_manager TEXT)")
#cursor.execute("CREATE TABLE info_clasificacion (id TEXT, proceso TEXT, nombre TEXT,descripcion TEXT, tipo TEXT, categoria TEXT, medio_conservacion TEXT, ubicacion TEXT, owner TEXT, estado TEXT, confidencialidad TEXT, integridad TEXT, disponibilidad TEXT, criticidad TEXT)")
#cursor.execute("CREATE TABLE relacion_funcionarios (user_id INTEGER, proceso TEXT, user_manager TEXT, owner TEXT, mail_manager TEXT, mail_owner TEXT)")


#Convertir a lista el csv y llenar tabla info_usuarios
tabla_info_users = leer_insumos.cargar_csv() 
items = list(tabla_info_users.items())
print(items)
cursor.executemany("INSERT INTO info_usuarios VALUES(?,?,?,?)", items)

#Convertir a lista el json y llenar la tabla info_clasificacion
#tabla_info_clas = leer_insumos.cargar_json()
#cursor.executemany("INSERT INTO info_clasificacion VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", tabla_info_clas)

#Convertir a lista el excel y llenar la tabla relacion_funcionarios
#tabla_relacion_funcionarios = leer_insumos.cargar_excel()
#to_records_relacion_funcionarios = tabla_relacion_funcionarios.to_records(index=False)
#list_relacion_funcionarios = list(to_records_relacion_funcionarios)
#cursor.executemany("INSERT INTO info_usuarios VALUES(?,?,?,?,?,?)", list_relacion_funcionarios)


conexion.commit()
conexion.close()