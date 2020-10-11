# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import asignacion_tablas

#Crear conexión y cursor
conexion = sqlite3.connect("Database")
cursor = conexion.cursor()

#Crear Tablas
#cursor.execute("CREATE TABLE info_usuarios (row_id INTEGER PRIMARY KEY, user_id INTEGER,user_manager TEXT)")
#cursor.execute("CREATE TABLE info_clasificacion (id TEXT PRIMARY KEY, nombre TEXT,descripcion TEXT, tipo TEXT, categoria TEXT, medio_conservacion TEXT, ubicacion TEXT, owner TEXT, estado TEXT, confidencialidad TEXT, integridad TEXT, disponibilidad TEXT, criticidad TEXT)")
#cursor.execute("CREATE TABLE relacion_funcionarios (ID INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER, owner TEXT, proceso TEXT)")
#cursor.execute("CREATE TABLE manager (user_manager TEXT PRIMARY KEY, mail_manager TEXT)")
#cursor.execute("CREATE TABLE owner (owner TEXT PRIMARY KEY, mail_owner TEXT)")
#cursor.execute("CREATE TABLE user (user_id INTEGER PRIMARY KEY, user_state TEXT)")

#Llenar tabla info_usuarios
#tabla_info_users = asignacion_tablas.info_users()
#cursor.executemany("INSERT INTO info_usuarios VALUES (?,?,?)", tabla_info_users)

#Llenar la tabla info_clasificacion
#tabla_info_clas = asignacion_tablas.info_clasificacion()
#cursor.executemany("INSERT INTO info_clasificacion VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", tabla_info_clas)

#Llenar la tabla relacion_funcionarios
#tabla_relacion_funcionarios = asignacion_tablas.relacion_funcionarios()
#cursor.executemany("INSERT INTO relacion_funcionarios VALUES (NULL,?,?,?)", tabla_relacion_funcionarios)

#Llenar la tabla manager
#tabla_manager = asignacion_tablas.manager()
#cursor.executemany("INSERT INTO manager VALUES (?,?)", tabla_manager)

#Llenar la tabla owner
#tabla_owner = asignacion_tablas.owner()
#cursor.executemany("INSERT INTO owner VALUES (?,?)", tabla_owner)

#Llenar la tabla manager
#tabla_user = asignacion_tablas.user()
#cursor.executemany("INSERT INTO user VALUES (?,?)", tabla_user)

conexion.commit()
conexion.close()