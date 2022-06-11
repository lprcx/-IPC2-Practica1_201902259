from platform import node


class NodoCliente():
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None

class Cliente():
    def __init__(self, idc, nombre):
        self.idcliente = idc
        self.nombre = nombre
        self.carrito = None

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0

    def Insertar(self, cliente):
        nuevo = NodoCliente(cliente)
        nuevo.siguiente=self.cabeza
        self.cabeza=nuevo
        self.tamanio+=1

    def AgregarCarrito(self, idc, idcarrito):
        cliente = self.ObtenerCliente(idc)
        if cliente!= None:
            cliente.cliente.carrito=idcarrito
            print("El cliente " + cliente.cliente.nombre + " ha tomado el carrito " + str(idcarrito))
        else:
            print("Cliente no encontrado")

    def ObtenerCliente(self, idc):
        actual=self.cabeza
        while(actual!=None):
            if actual.cliente.idcliente==idc:
                return actual
            actual=actual.siguiente
        return None

    def MostrarCliente(self, idc):
        cliente = self.ObtenerCliente(idc)
        print("Nombre del Cliente: " + cliente.cliente.nombre)
        print("Carrito: " + str(cliente.cliente.carrito))

    def Eliminar(self, idc):
        temporal = self.ObtenerCliente(idc)
        if temporal!=None:
            if temporal==self.cabeza:
                aux=self.cabeza
                self.cabeza=self.cabeza.siguiente
                return aux.cliente
            else:
                actual=self.cabeza
                while(actual!=None):
                    if actual.siguiente == temporal:
                        actual.siguiente = temporal.siguiente
                        self.tamanio-=1
                        return temporal.cliente
                    actual=actual.siguiente
                return None
        else:
            print("No se encontró al cliente")
    
    def Mostrar(self):
        actual=self.cabeza
        while(actual!=None):
            print(actual.cliente.nombre + " - carro " + str(actual.cliente.carrito) + ", ", end="")
            actual=actual.siguiente