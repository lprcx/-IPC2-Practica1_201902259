from ast import Num


class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None
        self.anterior = None

class ListaDobleC:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def Insertar(self, numero):
        nuevo = Nodo(numero)
        if self.primero == self.ultimo==None:
            self.primero = nuevo
            self.ultimo = self.primero
            self.primero.siguiente = self.ultimo
            self.primero.anterior = self.ultimo
            self.ultimo.anterior = self.primero
            self.ultimo.siguiente = self.primero
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            self.ultimo.siguiente = self.primero
            self.primero.anterior = self.ultimo
        self.tamanio+=1

    def MostrarLista(self):
        temporal=self.primero
        contador=0
        while (contador!=self.tamanio):
            print(str(temporal.numero))
            temporal=temporal.siguiente
            contador+=1
    
    def Retornaractual(self, numero):
        actual=self.primero
        contador=0
        while (contador!=self.tamanio):
            if actual.numero==numero:
                return actual
            actual=actual.siguiente
            contador+=1
        return None

#Pruebas para mostrar en consola

numeros = ListaDobleC()
numeros.Insertar(3)
numeros.Insertar(6)
numeros.Insertar(9)
numeros.Insertar(12)
numeros.Insertar(15)
numeros.MostrarLista()
num=input("Seleccione un número: ")
actual=numeros.Retornaractual(int(num))
if actual!=None:
    print("Anterior: "+str(actual.anterior.numero))
    print("Actual: "+ str(actual.numero))
    print("Siguiente " + str(actual.siguiente.numero))
else:
    print("Seleccione un numero de la lista")