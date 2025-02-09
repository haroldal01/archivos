class ListaIndexada:
    def __init__(self, tamaño=10):
        self.lista = [None] * tamaño 
        self.indice = list(range(tamaño))  
        self.n = 0
        self.tamaño = tamaño

    def insertar(self, valor):
        if self.n < self.tamaño:
            self.lista[self.n] = valor
            self.n += 1
        else:
            print("Error: La lista está llena.")

    def mostrar(self):
        imprimir = "Lista Indexada:\n"
        for i in range(self.n):
            imprimir += f"Índice: {self.indice[i]} -> Valor: {self.lista[i]}\n"
        return imprimir.strip()  # Retorna la lista como string sin espacios extra

    def eliminar(self, idx):
        if idx < 0 or idx >= self.n:
            print("Error: Índice fuera de rango.")
            return
        
        for i in range(idx, self.n - 1):
            self.lista[i] = self.lista[i + 1]
        
        self.lista[self.n - 1] = None
        self.n -= 1
        print(f"Elemento en índice {idx} eliminado.")




