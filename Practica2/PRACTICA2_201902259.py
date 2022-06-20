from dis import disco
from gettext import Catalog
from logging import root
import xml.etree.ElementTree as et
import tkinter as tk
from tkinter import filedialog
import os
empresa= None
discos=None

def Carga():
    root = tk.Tk()
    root.withdraw()
    ruta = filedialog.askopenfilename(title="Carga de", filetypes=(("Text files", "*.xml*"), ("all files", "*.*")))
    archivo = et.parse(ruta)
    return archivo

def MenuCarga():
    global empresa
    global discos
    print("1. Cargar Empleados")
    print("2. Cargar Discos")
    opcion = int(input("Seleccione una opción: "))
    if opcion==1:
        empresa=Carga()
        if empresa!=None:
            print("SE cargaron correctamente los empleados")
        else:
            print("Ocurrió un error en el archivo :c")
    elif opcion==2:
        discos=Carga()
        if discos!=None:
            print("SE cargaron correctamente los discos")
        else:
            print("Ocurrió un error en el archivo :c")

def MenuEmpleados():
    while(True):
        try:
            print("1. Ver empleado")
            print("2. MOdificacion")
            print("3. Eliminacion")
            print("4. Ver todo")
            print("5. Generar archivo")
            print("6. Salir")
            print("Seleccione una opción")
            opcion = 0
            opcion = int(input())
            if opcion==1:
                VerEmpleado()
            elif opcion==2:
                ModificarEmpledo()
            elif opcion==3:
                Eliminar()
            elif opcion==4:
                VerTodo()
            elif opcion==5:
                GenerarArchivoEm()
            elif opcion==6:
                break
            else:
                print("Seleccione una opción válida")
        except:
            print("Seleccione una opción válida")

def VerEmpleado():
    global empresa
    empleados=empresa.getroot()
    if empleados!=None:
        id=int(input("Ingrese ID del empleado: "))
        for departamento in empleados:
            for empleado in departamento:
                if id == int(empleado.attrib.get("id")):
                    for e in empleado:
                        if e.tag=="nombre":
                            print("Nombre: " + e.text)
                        elif e.tag=="puesto":
                            print("Puesto: " + e.text)
                        elif e.tag=="salario":
                            print("Salario:" + e.text)
    else:
        print("Primero cargue el archivo de empleado")

def ModificarEmpledo():
    global empresa
    empleados=empresa.getroot()
    if empleados!=None:
        id=int(input("Ingrese ID del empleado: "))
        nombre=input("Ingrese el nuevo nombre del usuario: ")
        puesto=input("Ingrese el nuevo puesto del usuario: ")
        salario=input("Ingrese el nuevo salario del usuario: ")
        for departamento in empleados:
            for empleado in departamento:
                if id == int(empleado.attrib.get("id")):
                    for e in empleado:
                        if e.tag=="nombre":
                            e.text=nombre
                        elif e.tag=="puesto":
                            e.text=puesto
                        elif e.tag=="salario":
                            e.text = salario
                    print("Se ha actualizado correctamente el usuario")
    else:
        print("Primero cargue el archivo de empleado")    

def Eliminar():
    global empresa
    empleados=empresa.getroot()
    if empleados!=None:
        id=int(input("Ingrese ID del empleado: "))
        for departamento in empleados:
            for empleado in departamento:
                if id == int(empleado.attrib.get("id")):
                    departamento.remove(empleado)
                    print("Se ha eliminado el empleado")
    else:
        print("Primero cargue el archivo de empleado")

def VerTodo():
    global empresa
    empleados=empresa.getroot()
    if empleados!=None:
        print("Empresa: ")
        for departamento in empleados:
            print("Departamento: "+ departamento.attrib.get("departamento"))
            for empleado in departamento:
                print("Empleado con id: " + str(empleado.attrib.get("id")))
                for e in empleado:
                    if e.tag=="nombre":
                        print("Nombre: " + e.text)
                    elif e.tag=="puesto":
                        print("Puesto: " + e.text)
                    elif e.tag=="salario":
                        print("Salario:" + e.text)
def GenerarArchivoEm():
    global empresa
    empresa.write("empleados_actualizado.xml", "UTF-8")
    print("Archivo creado correctamente")


##discos

def MenuDiscos():
    while(True):
        try:
            print("1. Ver disco")
            print("2. MOdificacion")
            print("3. Eliminacion")
            print("4. Ver todo")
            print("5. Generar archivo")
            print("6. Salir")
            print("Seleccione una opción")
            opcion = int(input())
            if opcion==1:
                VerDiscos()
            elif opcion==2:
                ModificarDiscos()
            elif opcion==3:
                EliminarDisco()
            elif opcion==4:
                VerTodocd()
            elif opcion==5:
                GenerarArchivoDisco()
            elif opcion==6:
                break
            else:
                print("Seleccione una opción válida")
        except:
            print("Seleccione una opción válida")

def VerDiscos():
    global discos
    Catalog=discos.getroot()
    titulo = input("Ingrese el titulo del disco: ")
    for cd in Catalog:
        if cd[0].text==titulo:
            print("Titulo: " + cd[0].text)
            print("Artista: " + cd[1].text)
            print("País: " + cd[2].text)
            print("Compañía: " + cd[3].text)
            print("Precio: " + cd[4].text)
            print("Año: " + cd[5].text)

def ModificarDiscos():
    global discos
    Catalog=discos.getroot()
    titulo = input("Ingrese el titulo del disco: ")
    for cd in Catalog:
        if cd[0].text==titulo:
            cd[1].text=input("Ingrese el nuevo artista: ")
            cd[2].text=input("Ingrese el nuevo país: ")
            cd[3].text=input("Ingrese la nueva compañía: ")
            cd[4].text=input("Ingrese el nuevo precio: ")
            cd[5].text=input("Ingrese el nuevo año: ")
            print("Se ha actualizado el disco")


def EliminarDisco():
    global discos
    Catalog=discos.getroot()
    titulo = input("Ingrese el titulo del disco: ")
    for cd in Catalog:
        if cd[0].text==titulo:
            Catalog.remove(cd)
            print("Se ha eliminado el disco")

def VerTodocd():
    global discos
    Catalog=discos.getroot()
    print("--------------------------------")
    print("           Catalog              ")
    for cd in Catalog:
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("             cd              ")
        print("Titulo: " + cd[0].text)
        print("Artista: " + cd[1].text)
        print("País: " + cd[2].text)
        print("Compañía: " + cd[3].text)
        print("Precio: " + cd[4].text)
        print("Año: " + cd[5].text)

def GenerarArchivoDisco():
    global discos
    discos.write("discos_actualizado.xml", "UTF-8")
    print("Archivo Generado Correctamente")


def GenerarReporteEmpleados():
    global empresa
    empleados = empresa.getroot()
    codigo="digraph G {\nnode[shape=\"box\"];\n empresa[label=\"empresa\"];\n"
    for i in range(len(empleados)):
        codigo+="departamento_"+str(i)+"[label=\"departamento="+empleados[i].attrib.get("departamento")+"\"];\n"
        codigo+="empresa->departamento_"+str(i)+";\n"
        for j in range(len(empleados[i])):
            codigo+="empleado"+str(i)+str(j)+"[label=\"empleado id "+empleados[i][j].attrib.get("id")+"\"];\n"
            codigo+="departamento_"+str(i)+"->empleado"+str(i)+str(j)+";\n"
            for k in range(len(empleados[i][j])):
                codigo+="e"+str(i)+str(j)+str(k)+"[label=\""+empleados[i][j][k].tag+":"+empleados[i][j][k].text+"\"];\n"
                codigo+="empleado"+str(i)+str(j)+"->e"+str(i)+str(j)+str(k)+";\n"
    codigo+="}"
    file=open("ReporteEmpleados.dot", "w")
    file.write(codigo)
    file.close()
    os.system("dot -Tpng ReporteEmpleados.dot -o ReporteEmpleados.png")
    os.startfile("ReporteEmpleados.png")
    print("Reporte de Empleados Generado con Éxito")

def ReporteDiscos():
    global discos
    Catalog=discos.getroot()
    codigo = 'digraph G {node[shape=\"box\"];\nCatalog[label=\"catalog\"];\n'
    for i in range(len(Catalog)):
        codigo += 'CD_' +str(i)+'[label=\"' + Catalog[i].tag + '\"];\n'
        codigo += 'Catalog->CD_'+ str(i) + ';\n'
        for j in range(len(Catalog[i])):
            txt = Catalog[i][j].text.replace('"','')
            txt = txt.replace("'",'')
            codigo+= 'CD' + str(i) + str(j) + '[label=\"' + Catalog[i][j].tag + ":" + txt + '\"];\n'
            codigo += 'CD_'+ str(i) + '->CD' + str(i) + str(j) + ';\n'
    codigo+="}"
    file=open("ReporteDiscos.dot", "w")
    file.write(codigo)
    file.close()
    os.system("dot -Tpng ReporteDiscos.dot -o ReporteDiscos.png")
    os.startfile("ReporteDiscos.png")
    print("Reporte de Discos Generado con Éxito")

def MenuReportes():
    print("1. Generar Reporte de Empleados")
    print("2. Generar Reporte de Discos")
    opcion = int(input("Seleccione una opción: "))
    if opcion==1:
        GenerarReporteEmpleados()
    elif opcion==2:
        ReporteDiscos()


def Menu():
    while(True):
        try:
            print("------------MENÚ PRINCIPAL-----------")
            print("1. Carga de datos")
            print("2. Gestion de empleados")
            print("3. Gestión de Discos")
            print("4. Reportes")
            print("5. Salir")
            print("Seleccione una opción")
            opcion = 0
            opcion = int(input())
            if opcion==1:
                MenuCarga()
            elif opcion==2:
                MenuEmpleados()
            elif opcion==3:
                MenuDiscos()
            elif opcion==4:
                MenuReportes()
            elif opcion==5:
                break
            else:
                print("Seleccione una opción válida")
        except:
            print("Seleccione una opción válida")
Menu()