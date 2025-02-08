class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

class ListaLigada:
    def __init__(self):
        self.head = None

    def add(self, dato):
        new_node = Nodo(dato)
        if self.head is None:
            self.head = new_node
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = new_node

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
        return True

    def show(self):
        actual = self.head
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.next
        print("None")

