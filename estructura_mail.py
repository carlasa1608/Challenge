# -*- coding: utf-8 -*-

import espacios_vacios
import leer_insumos

info_vacia = espacios_vacios.espacio_vacio()
info_clas_alto = espacios_vacios.arreglar_espacios()
info_funcionarios = leer_insumos.cargar_excel()

def cuerpo_correo():
    global matriz_estructura
    owners = info_clas_alto[8].values.tolist()
    estado = info_clas_alto[9].values.tolist()
    criticidad = info_clas_alto[13].values.tolist()
    id_base = info_clas_alto[0].values.tolist()
    proceso = info_clas_alto[1].values.tolist()
    nombre = info_clas_alto[2].values.tolist()
    descripcion = info_clas_alto[3].values.tolist()
    tipo = info_clas_alto[4].values.tolist()
    categoria = info_clas_alto[5].values.tolist()
    medio = info_clas_alto[6].values.tolist()
    ubicacion = info_clas_alto[7].values.tolist()
    confidencialidad = info_clas_alto[10].values.tolist()
    integridad = info_clas_alto[11].values.tolist()
    disponibilidad = info_clas_alto[12].values.tolist()
    cuerpo_mail = owners
    long_n = len(info_clas_alto)
    atributos = ["id","proceso", "nombre","descripcion","tipo","categoria",
                 "medio_conservacion","ubicacion","owner","estado",
                 "confidencialidad","integridad","disponibilidad","criticidad"]
    for n in range(long_n):
        if info_vacia == "id":
            id_base[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "proceso":
            proceso[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "nombre":
            nombre[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "descripcion":
            descripcion[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "tipo":
            tipo[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "categoria":
            categoria[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "medio_conservacion":
            medio[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "ubicacion":
            ubicacion[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "confidencialidad":
            confidencialidad[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "integridad":
            integridad[n] = "Se requiere actualizar este dato, pues no se encuentra"
        elif info_vacia == "disponibilidad":
            disponibilidad[n] = "Se requiere actualizar este dato, pues no se encuentra"
        
        cuerpo_mail[n] = ("Buen día "+owners[n]
                          +". \n\n¡Hemos mejorado la revalidación anual del proceso de clasificación de la información! \nA continuación encontará la información relacionada con la base en la cual usted figura como propietario. Si se encuentra de acuerdo con la información suministrada responda este email con un OK. \n\nEn caso de tener que actulizar datos, junto con la información de la base se indica cuál es el dato a actualizar, por favor indique el nombre del campo:el dato actualizado previo al OK. \n\n"
                          +"id: "+id_base[n]+" \nproceso: "+proceso[n]+"\nnombre: "+nombre[n]
                          +" \ndescripcion: "+descripcion[n]+"\ntipo: "+tipo[n]
                          +" \ncategoria: "+categoria[n]+"\nmedio de conservacion: "+medio[n]
                          +" \nubicacion: "+ubicacion[n]+"\nowner: "+owners[n]
                          +" \nestado: Activo"+"\nconfidencialidad: "+confidencialidad[n]
                          +" \nintegridad: "+integridad[n]+"\ndisponibilidad: "+disponibilidad[n]
                          +" \ncriticidad: Alto"+" \n\nDe antemano muchas gracias.")
    return cuerpo_mail
       
def info_correo():
    global info_mail
    owners_mail = info_clas_alto[8].values.tolist()
    manager_mail = info_clas_alto[8].values.tolist()
    nombre_base = info_clas_alto[2].values.tolist()
    clasificacion = info_clas_alto[8].values.tolist()
    long_m = len(info_funcionarios)
    long_l = len(owners_mail)
    for l in range(long_l):
        clasificacion[l] = "Alto"
        for m in range(long_m):
            if info_funcionarios[m][3] == owners_mail[l]:
                owners_mail[l] = info_funcionarios[m][5]
                manager_mail[l] = info_funcionarios[m][4]
    z = 4
    info_mail = []
    for i in range(long_l):
        info_mail.append([nombre_base[i],owners_mail[i],manager_mail[i],clasificacion[i]])
    return info_mail
    
cuerpo_correo()
info_correo()