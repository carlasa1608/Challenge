# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas
from pandas import ExcelWriter
import sys
import os

root = Tk() #A root se le asigna la función Tkinter (Tk), la cual contiene todas las funcionalidades de 
root.title('Mercado libre')
root.geometry("800x800+100+100")
    
Button(root, text='RunR', anchor='n').grid(row=4, column=0, pady=10) #Que se genere un boton

mainloop()