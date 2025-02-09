class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaLigada:
    def __init__(self, indice):
        self.head = None
        self.indice = indice  
        self.counter = 0  

    def add(self, dato):
        if self.counter >= self.indice:  # Verifica si se alcanzó el límite
            print("No se pueden agregar más elementos. Límite alcanzado.")
            return

        new_node = Nodo(dato)
        if self.head is None:
            self.head = new_node
        else:
            actual = self.head  # Se corrige la referencia
            while actual.next:
                actual = actual.next
            actual.next = new_node

        self.counter += 1  # Aumenta el contador

    def delete(self, dato):
        actual = self.head
        previous = None
        while actual and actual.dato != dato:
            previous = actual
            actual = actual.next
        if actual is None:
            return False
        if previous is None:
            self.head = actual.next
        else:
            previous.next = actual.next

        self.counter -= 1 
        return True

    def show(self):
        actual = self.head
        imprimir = ""

        while actual:
            imprimir += str(actual.dato + "->")
            actual = actual.next
        
        return imprimir 
