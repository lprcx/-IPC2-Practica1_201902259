from Pila import Pila
from ListaEnlazada import Cliente, ListaEnlazada
from Cola import Cola
pila_carritos=Pila()
lista_clientes=ListaEnlazada()
cola_pagos=Cola()

def Ingresodatos():
    global pila_carritos
    cantidad=int(input("Ingrese la cantidad de carritos: \n=>"))
    if cantidad>0:
        if pila_carritos.tamanio==0:
            contador=0
            while(contador!=cantidad):
                pila_carritos.Push(contador+1)
                contador+=1
        else:
            ultimo=pila_carritos.tamanio
            contador=0
            while(contador!=cantidad):
                pila_carritos.Push(ultimo+contador+1)
                contador+=1
        print("Carritos agregados con éxito")
        pila_carritos.Mostrar()
    else:
        print("Ingrese un número válido de carritos")

contador_clientes=1
def NuevoCliente():
    global contador_clientes
    nombre=input("Ingrese el nombre del nuevo cliente: ")
    id=contador_clientes
    carro = pila_carritos.Pop()
    if carro!= None:
        nuevo = Cliente(id, nombre)
        lista_clientes.Insertar(nuevo)
        lista_clientes.AgregarCarrito(id, carro.id)
        contador_clientes+=1
        print("Cliente agregado con éxito con ID: " + str(id))
    else:
        print("No se pudo agregar al cliente, no hay carritos disponibles")

def VerCliente():
    global lista_clientes
    global cola_pagos
    idc = input("Ingrese el ID del cliente: ")
    if lista_clientes.ObtenerCliente(int(idc))!=None:
        lista_clientes.MostrarCliente(int(idc))
        opcion = input("Desea Pagar? (S/N): ")
        if opcion == "S":
            cliente = lista_clientes.Eliminar(int(idc))
            cola_pagos.Encolar(cliente)
            print("Cliente agregado a cola de caja")
        elif opcion == "N":
            pass
        else:
            print("Seleccione una opción válida")
    else:
        print("Cliente no encontrado")

def CajaRegistradora():
    if cola_pagos.cabeza!=None:
        print("Se está atendiendo actualmente al cliente " + cola_pagos.cabeza.cliente.nombre)
        print("1. Avanzar")
        print("2. Regresar")
        opcion = int(input("Ingrese una opción: "))
        if opcion==1:
            print("El cliente ha salido de la cola")
            cliente=cola_pagos.Desencolar()
            carrito = cliente.carrito
            pila_carritos.Push(carrito)
        elif opcion ==2:
            pass
        else:
            print("Seleccione una opción válida")

def VisualizarDatos():
    print("Pila de Carritos: ")
    pila_carritos.Mostrar()
    print("\nLista Usuarios: ")
    lista_clientes.Mostrar()
    print("\nCola Caja Registradora: ")
    cola_pagos.Mostrar()
    print("")

def Menu():
    while(True):
        try:
            print("------------MENÚ PRINCIPAL-----------")
            print("1. Ingreso de datos")
            print("2. Nuevo Cliente")
            print("3. Ver Cliente")
            print("4. Caja Registradora")
            print("5. Visualizar Datos")
            print("6. Salir")
            print("Seleccione una opción")
            opcion = 0
            opcion = int(input())
            if opcion==1:
                Ingresodatos()
            elif opcion==2:
                NuevoCliente()
            elif opcion==3:
                VerCliente()
            elif opcion==4:
                CajaRegistradora()
            elif opcion==5:
                VisualizarDatos()
            elif opcion==6:
                break
            else:
                print("Seleccione una opción válida")
        except:
            print("Seleccione una opción válida")
Menu()