class Nodo:
    def __init__(self, id):
        self.id = id
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def Push(self, id):
        nuevo = Nodo(id)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamanio+=1
    
    def Pop(self):
        if self.tamanio>0:
            temporal = self.cabeza
            self.cabeza = self.cabeza.siguiente
            self.tamanio-=1
            return temporal
        else:
            return None

    def Mostrar(self):
        actual=self.cabeza
        while(actual!=None):
            print(str(actual.id) + ", ", end="")
            actual=actual.siguiente
            