# -*- coding: utf-8 -*-

import os
import csv
import json
import pandas as pd
os.chdir("C:/Users/Admin/Documents/Mercado Libre/Caso - JSON y CSV en Base de Datos")
        
def cargar_csv():
    global info_users
    #info_users = pd.read_csv('info_usuarios.csv',header=0)
    with open('info_usuarios.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            info_users = row
            print(info_users)
    return info_users

def cargar_excel():
    global relacion_funcionarios
    relacion_funcionarios = pd.read_excel('relacion_funcionarios.xlsx', sheet_name='Hoja1')
    return relacion_funcionarios

def cargar_json(): #Función para cargar el archivo json
    cargar_excel()
    global info_clas
    global espacio_vacio
    with open('crear_json.json') as cont_json:
        info_clas = json.load(cont_json)
    long=len(relacion_funcionarios)
    longitud = (len(info_clas)-1)
    atributos = ["id","proceso", "nombre","descripcion","tipo","categoria",
                 "medio_conservacion","ubicacion","owner","estado",
                 "confidencialidad","integridad","disponibilidad","criticidad"]
    for i in range(longitud):
        for n in atributos:
            if info_clas[i]["criticidad"] == "Alto":
                if info_clas[i]["estado"] != "Inactivo":
                    if len(info_clas[i][n]) < 1:
                        if n == atributos[0]:
                            espacio_vacio = (i,n)
                            info_clas = ("BD")
                        elif n == atributos[1]:
                            for m in relacion_funcionarios:
                                if m == 'owner':
                                    for l in range(long):
                                        if relacion_funcionarios[m][l] == info_clas[i]['owner']:
                                            info_clas[i][n] = relacion_funcionarios['proceso'][l]
                        elif n == atributos[2]:
                            espacio_vacio = (i,n)
                            info_clas = ("Nombre vacio")
                        elif n == atributos[3]:
                            espacio_vacio = (i,n)
                            info_clas = ("Descripcion vacio")
                        elif n == atributos[4]:
                            espacio_vacio = (i,n)
                            info_clas = ("Tipo vacio")
                        elif n == atributos[5]:
                            espacio_vacio = (i,n)
                            info_clas = ("Categoria vacio")
                        elif n == atributos[6]:
                            espacio_vacio = (i,n)
                            info_clas = ("Medio de conservacion vacio")
                        elif n == atributos[7]:
                            espacio_vacio = (i,n)
                            info_clas = ("Ubicacion vacio")
                        elif n == atributos[8]:
                            for m in relacion_funcionarios:
                                if m == 'proceso':
                                    for l in range(long):
                                        if relacion_funcionarios[m][l] == info_clas[i]['proceso']:
                                            info_clas[i][n] = relacion_funcionarios['owner'][l]
                                            break
                        elif n == atributos[9]:
                            info_clas[i][n] = "Activo"
                        elif n == atributos[10]:
                            info_clas[i][n] = "Alto"
                            espacio_vacio = (i,n)
                        elif n == atributos[11]:
                            info_clas[i][n] = "Alto"
                            espacio_vacio = (i,n)
                        elif n == atributos[12]:
                            info_clas[i][n] = "Alto"
                            espacio_vacio = (i,n)
                        elif n == atributos[13]:
                            info_clas[i][n] = "Alto"
                            espacio_vacio = (i,n)
                        else:
                            espacio_vacio = 0
    return espacio_vacio
    return info_clas
    

#if __name__ == '__main__':
#    cargar_json()
#    cargar_csv()
#    cargar_excel()


