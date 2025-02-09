class ListaContigua:
    def __init__(self, tamaño=10):
        self.lista = [None] * tamaño  
        self.tamaño = tamaño
        self.n = 0 
    
    def ingresar(self, valor):
        
        if self.n < self.tamaño:
            self.lista[self.n] = valor
            self.n += 1
        else:
            print("Error: La lista está llena.")
    
    def eliminar(self, indice):
        
        if 0 <= indice < self.n:
            for i in range(indice, self.n - 1):
                self.lista[i] = self.lista[i + 1]
            self.lista[self.n - 1] = None
            self.n -= 1
        else:
            print("Error: Índice fuera de rango.")
    
    def mostrar(self):
        
        return "Lista Contigua:", [self.lista[i] for i in range(self.n)]

    



