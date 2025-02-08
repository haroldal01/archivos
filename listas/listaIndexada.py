class ListaIndexada:
    """Clase que representa una lista indexada."""
    
    def __init__(self, tamaño=10):
        self.lista = [None] * tamaño 
        self.indice = [None] * tamaño 
        self.n = 0 

    def insertar(self, valor):
        """Inserta un nuevo elemento en la lista con su índice."""
        if self.n < len(self.lista):
            self.lista[self.n] = valor
            self.indice[self.n] = self.n  
            self.n += 1
        else:
            print("Error: La lista está llena.")

    def mostrar(self):
        """Muestra los elementos de la lista indexada."""
        print("Lista Indexada:")
        for i in range(self.n):
            print(f"Índice: {self.indice[i]} -> Valor: {self.lista[i]}")



