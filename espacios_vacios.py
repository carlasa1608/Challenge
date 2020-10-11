# -*- coding: utf-8 -*-

import leer_insumos 
import pandas as pd

def arreglar_espacios():
    global new_table
    global espacio_blanco
    espacio_blanco = 100
    insumo_json = pd.DataFrame(leer_insumos.cargar_json())
    insumo_excel = pd.DataFrame(leer_insumos.cargar_excel())
    new_table = insumo_json
    longitud_a = (len(insumo_json))
    longitud_b = (len(insumo_excel))
    for a in range(longitud_a):
        if insumo_json[9][a] == "Inactivo":
            new_table = new_table.drop([a],axis=0)
        elif insumo_json[9][a] == " ":
            new_table[9][a] = "Activo"
        else:
            if insumo_json[13][a] == "Alto":
                if insumo_json[8][a] == " ":
                    for b in range(longitud_b):
                        if insumo_excel[1][b] == insumo_json[1][a]:
                            new_table[8][a] = insumo_excel[3][b]
                            break
                else:
                    for c in range(12):
                        if insumo_json[c][a] == " ":
                            espacio_blanco = c
            elif insumo_json[13][a] == " ":
                new_table[13][a] = "Alto"
            else:
                new_table = new_table.drop([a],axis=0)
    return new_table

def espacio_vacio():
    global info_blanco
    atributos = ["id","proceso", "nombre","descripcion","tipo","categoria",
                 "medio_conservacion","ubicacion","owner","estado",
                 "confidencialidad","integridad","disponibilidad","criticidad"]
    if espacio_blanco == 0:
        info_blanco = atributos[0]
    elif espacio_blanco == 1: 
        info_blanco = atributos[1]
    elif espacio_blanco == 2: 
        info_blanco = atributos[2]
    elif espacio_blanco == 3: 
        info_blanco = atributos[3]
    elif espacio_blanco == 4: 
        info_blanco = atributos[4]
    elif espacio_blanco == 5: 
        info_blanco = atributos[5]
    elif espacio_blanco == 6: 
        info_blanco = atributos[6]
    elif espacio_blanco == 7: 
        info_blanco = atributos[7]
    elif espacio_blanco == 10: 
        info_blanco = atributos[10]
    elif espacio_blanco == 11: 
        info_blanco = atributos[11]
    elif espacio_blanco == 12: 
        info_blanco = atributos[12]
    else:
        info_blanco = "NA"
    return info_blanco
    
arreglar_espacios()
espacio_vacio()