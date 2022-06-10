from Pila import Pila
pila_carritos=Pila()

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
        

def Menu():
    while(True):
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
            pass
        elif opcion==3:
            pass
        elif opcion==4:
            pass
        elif opcion==5:
            pass
        elif opcion==6:
            break
        else:
            print("Seleccione una opción válida")
    
Menu()