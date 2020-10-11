# -*- coding: utf-8 -*-

import os
import pandas as pd
os.chdir("C:/Users/Admin/Documents/Mercado Libre/Caso - JSON y CSV en Base de Datos")
        
def cargar_csv(): #Función para cargar el archivo csv
    global info_users
    df = pd.read_csv('info_usuarios.csv',header=0)    
    info_users = df.values.tolist()
    return info_users

def cargar_excel(): #Función para cargar el archivo xlsx
    global relacion_funcionarios
    df = pd.read_excel('relacion_funcionarios.xlsx', sheet_name='Hoja1')
    relacion_funcionarios = df.values.tolist()
    return relacion_funcionarios

def cargar_json(): #Función para cargar el archivo json
    global info_clas
    df = pd.read_json('crear_json.json')
    info_clas = df.values.tolist()
    return info_clas

if __name__ == '__main__':
    cargar_json()
    cargar_csv()
    cargar_excel()
