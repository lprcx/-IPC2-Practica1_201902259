class Nodoji():
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None
    
class Cola():
    def __init__(self):
        self.cabeza = None
    
    def Encolar(self, cliente):
        nuevo = Nodoji(cliente)
        if self.cabeza==None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while(actual!=None):
                actual = actual.siguiente
                break
            actual.siguiente = nuevo
    
    def Desencolar(self):
        if self.cabeza == None:
            return None
        else:
            temporal = self.cabeza
            self.cabeza = self.cabeza.siguiente
            return temporal.cliente
            
    def Mostrar(self):
        actual=self.cabeza
        while(actual!=None):
            print(actual.cliente.nombre + " - carro " + str(actual.cliente.carrito) + ", ", end="")
            actual=actual.siguiente