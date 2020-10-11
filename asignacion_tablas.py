# -*- coding: utf-8 -*-

import leer_insumos

def info_users():
    global tabla_info_users
    tabla_info_users = []
    long_a = len(leer_insumos.cargar_csv())
    for a in range(long_a):
        row_id = leer_insumos.cargar_csv()[a][0]
        user_id = leer_insumos.cargar_csv()[a][1]
        user_manager = leer_insumos.cargar_csv()[a][3]
        tabla_info_users.append([row_id,user_id,user_manager])
    return tabla_info_users

def info_clasificacion():
    global tabla_info_clas
    tabla_info_clas = []
    long_b = len(leer_insumos.cargar_json())
    for b in range(long_b):
        id_base = leer_insumos.cargar_json()[b][0]
        nombre = leer_insumos.cargar_json()[b][2]
        descripcion = leer_insumos.cargar_json()[b][3]
        tipo = leer_insumos.cargar_json()[b][4]
        categoria = leer_insumos.cargar_json()[b][5]
        medio_conservacion = leer_insumos.cargar_json()[b][6]
        ubicacion = leer_insumos.cargar_json()[b][7]
        owner = leer_insumos.cargar_json()[b][8]
        estado = leer_insumos.cargar_json()[b][9]
        confidencialidad = leer_insumos.cargar_json()[b][10]
        integridad = leer_insumos.cargar_json()[b][11]
        disponibilidad = leer_insumos.cargar_json()[b][12]
        criticidad = leer_insumos.cargar_json()[b][13]
        tabla_info_clas.append([id_base,nombre,descripcion,tipo,categoria,medio_conservacion,ubicacion,owner,estado,confidencialidad,integridad,disponibilidad,criticidad])
    return tabla_info_clas
    
def relacion_funcionarios():
    global tabla_relacion_funcionarios
    tabla_relacion_funcionarios = []
    long_c = len(leer_insumos.cargar_excel())
    for c in range(long_c):
        user_id = leer_insumos.cargar_excel()[c][0]
        owner = leer_insumos.cargar_excel()[c][3]
        proceso = leer_insumos.cargar_excel()[c][1]
        tabla_relacion_funcionarios.append([user_id,owner,proceso])
    return tabla_relacion_funcionarios

def manager():
    global tabla_manager
    tabla_manager = []
    long_d = len(leer_insumos.cargar_excel())
    for d in range(long_d):
        user_manager = leer_insumos.cargar_excel()[d][2]
        mail_manager = leer_insumos.cargar_excel()[d][4]
        tabla_manager.append([user_manager,mail_manager])
    return tabla_manager

def owner():
    global tabla_owner
    tabla_owner = []
    long_e = len(leer_insumos.cargar_excel())
    for e in range(long_e):
        owner = leer_insumos.cargar_excel()[e][3]
        mail_owner = leer_insumos.cargar_excel()[e][5]
        tabla_owner.append([owner,mail_owner])
    return tabla_owner

def user():
    global tabla_user
    tabla_user = []
    long_f = len(leer_insumos.cargar_csv())
    for f in range(long_f):
        user_id = leer_insumos.cargar_csv()[f][1]
        user_state = leer_insumos.cargar_csv()[f][2]
        tabla_user.append([user_id,user_state])
    return tabla_user

info_users()    
info_clasificacion()
relacion_funcionarios()
manager()
owner()
user()