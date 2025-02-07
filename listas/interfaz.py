import tkinter as tk

def abrir_nueva_ventana(tipo):
    nueva_ventana = tk.Toplevel(ventana)  # Crear una nueva ventana
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("250x200")
    
    etiqueta = tk.Label(nueva_ventana, text="Ingrese el dato")
    etiqueta.pack(pady=5)
    
    entrada = tk.Entry(nueva_ventana)
    entrada.pack(pady=5)

    def leer_texto():
        texto = entrada.get()
        
        if tipo == "contigua":
            print("contigua")

        elif tipo == "ligadaSimple":
            print("ligada")

        elif tipo == "doble":
            print("doble")

        elif tipo == "indexada":
            print("indexada")
        

    btnInsertar = tk.Button(nueva_ventana, text="Insertar", command=leer_texto)
    btnInsertar.pack(pady=5)

    btnEliminar = tk.Button(nueva_ventana, text="Eliminar", command=leer_texto)
    btnEliminar.pack(pady=5)

    btnMostrar = tk.Button(nueva_ventana, text="Mostrar datos", command=leer_texto)
    btnMostrar.pack(pady=5)





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
