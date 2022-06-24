from dis import disco
from gettext import Catalog
from logging import root
import xml.etree.ElementTree as et
import tkinter as tk
from tkinter import filedialog
import os
discos=None

def Carga():
    root = tk.Tk()
    root.withdraw()
    ruta = filedialog.askopenfilename(title="Carga de", filetypes=(("Text files", "*.xml*"), ("all files", "*.*")))
    archivo = et.parse(ruta)
    return archivo


def Menuc():
    global discos
    print("1. Cargar Discos")
    opcion = int(input("Seleccione una opción: "))
    if opcion==1:
        discos=Carga()
        if discos!=None:
            print("SE cargaron correctamente los discos")
        else:
            print("Ocurrió un error en el archivo :c")
    else:
        print("Ingrese la opción correcta")

Menuc()


def VerDiscos():
    global discos
    Catalog=discos.getroot()
    anio = input("Ingrese el año del disco: ")
    for cd in Catalog:
        if cd[5].text==anio:
            print("Titulo: " + cd[0].text)
            print("Artista: " + cd[1].text)
            print("País: " + cd[2].text)
            print("Compañía: " + cd[3].text)
            print("Precio: " + cd[4].text)
            print("Año: " + cd[5].text)
            print("------------------------")
VerDiscos()