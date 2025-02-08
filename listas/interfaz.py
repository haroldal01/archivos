import tkinter as tk
from listaContigua import ListaContigua
from listaLigada import ListaLigada
from dobleLigada import ListaDoblemeteLigada
from listaIndexada import ListaIndexada


Contigua = ListaContigua()
Ligada = ListaLigada()
Doble = ListaDoblemeteLigada()
Indexada = ListaIndexada()

def abrir_nueva_ventana(tipo):

    def habilitar():
        btnIndice.config(state="normal")
        entradaIndice.config(state="normal")

    def leer_texto():
        texto = entrada.get()
        
        if tipo == "contigua":
            Contigua.ingresar(texto)
            Contigua.mostrar()

        elif tipo == "ligadaSimple":
            Ligada.add(texto)
            Ligada.show()

        elif tipo == "doble":
            Doble.add(texto)
            Doble.show()

        elif tipo == "indexada":
            Indexada.insertar(texto)

    def eliminar_dato():
        datoEliminado = int(entradaEliminar.get())
        if tipo == "contigua":
            Contigua.eliminar(datoEliminado)
            Contigua.mostrar()

        elif tipo == "ligadaSimple":
            Ligada.delete(datoEliminado)
            Ligada.show()

        elif tipo == "doble":
            Doble.delete(datoEliminado)
            Doble.show()

        elif tipo == "indexada":
            print("indexada")
            habilitar()  # Habilita los elementos al intentar eliminar en lista indexada

    nueva_ventana = tk.Toplevel(ventana) 
    nueva_ventana.geometry("290x300")
    
    etiqueta = tk.Label(nueva_ventana, text="Ingrese el dato")
    etiqueta.pack(pady=5)
    
    entrada = tk.Entry(nueva_ventana)
    entrada.pack(pady=5)

    btnInsertar = tk.Button(nueva_ventana, text="Insertar", command=leer_texto)
    btnInsertar.pack(pady=5)

    etiquetaEliminar = tk.Label(nueva_ventana, text="Escriba el índice del dato que eliminará")
    etiquetaEliminar.pack(pady=5)

    entradaEliminar = tk.Entry(nueva_ventana)
    entradaEliminar.pack(pady=5)

    btnEliminar = tk.Button(nueva_ventana, text="Eliminar", command=eliminar_dato)
    btnEliminar.pack(pady=5)

    btnMostrar = tk.Button(nueva_ventana, text="Mostrar datos", command=leer_texto)
    btnMostrar.pack(pady=5)

    btnIndice = tk.Button(nueva_ventana, text="Ingrese el tamaño de la lista indexada (máximo 10)", state="disabled")
    btnIndice.pack(pady=5)

    entradaIndice = tk.Entry(nueva_ventana, state="disabled")
    entradaIndice.pack(pady=5)

    # Si el tipo es "indexada", habilitar los elementos inmediatamente
    if tipo == "indexada":
        habilitar()




def accion_ListaContigua():
    abrir_nueva_ventana("contigua")

def accion_ListaLigadaSimple():
    abrir_nueva_ventana("ligadaSimple")

def accion_ListaDoblementeLigada():
    abrir_nueva_ventana("doble")

def accion_ListaIndexada():
    abrir_nueva_ventana("indexada")


ventana = tk.Tk()
ventana.title("Listas")  
ventana.geometry("300x200") 


boton1 = tk.Button(ventana, text="Lista Contigua (Arreglo)", command=accion_ListaContigua)
boton1.pack(pady=5)  # Agrega espaciado entre botones

boton2 = tk.Button(ventana, text="Lista Ligada (Simple)", command=accion_ListaLigadaSimple)
boton2.pack(pady=5)

boton3 = tk.Button(ventana, text="Lista Doblemente Ligada", command=accion_ListaDoblementeLigada)
boton3.pack(pady=5)

boton4 = tk.Button(ventana, text="Lista Indexada", command=accion_ListaIndexada)
boton4.pack(pady=5)

btnSalir = tk.Button(ventana, text="Salir", command=ventana.quit)
btnSalir.pack(pady=5)

ventana.mainloop()
