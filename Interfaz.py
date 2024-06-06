import os
import tkinter as tk #Se importa tkinter y se le asigna el nombre de TK
from tkinter import filedialog as FileSearch
from tkinter import messagebox as Message
import csv
from cifCesar import cifrar_cesar
from cifAffine import cifrar_affine
from cifMezcla import cifrar_mezcla

palabras = []

def leer_csv():
    file_path = FileSearch.askopenfilename(
        title="Selecciona el archivo",
        filetypes=(("Archivos CSV", "*.csv*"),)
        )
    #El punto csv ayuda a filtrar los archivos

    with open(file_path, newline="") as csvfile:
        reader= csv.reader(csvfile)
        global palabras
        for row in reader:
            palabras.append(row[0])

        contador = 0
        while contador < len(palabras):
            print(palabras[contador])
            mostrarRpta.insert(tk.END,palabras[contador] + "\n")##Solo sirve este codigo lo demás esta de relleno
            print("\n")

            contador = contador + 1

    #print("Prueba de botón")
    #print(palabras)


def cifradoCesar(mensaje):
    respuesta = "Cifrado Cesar: " + cifrar_cesar(mensaje, 3)
    mostrarEncrypt.insert(tk.END, respuesta)
    print("Sirve el cifrado cesar")
    ##LUEGO DE PRESIONAR EL BOTON QUE LLAMA A LA FUNCIÓN DEBE CREAR UN ARCHIVO CSV  

def cifradoAffline(mensaje):
    respuesta = "\nCifrado Affine: " + cifrar_affine(mensaje,23,5)
    mostrarEncrypt.insert(tk.END, respuesta)
    print("Sirve el cifrado Affine")


def cifradoMezcla(mensaje):
    respuesta = "\nCifrado Mezcla: " + cifrar_mezcla(mensaje,3,23,5)
    mostrarEncrypt.insert(tk.END, respuesta)
    print("Sirve el cifrado Mezcla")


##PARTE GRAFICA##
root=tk.Tk() 
root.title("Proyecto LP Encriptación")
root.geometry("1080x720") #Se asigna los valores de ancho y largo de la ventana

etiqueta = tk.Label(root, text="Texto de prueba")
etiqueta.pack() #el .pack hace que se muestre la variable en la que se aplicó


boton = tk.Button(root,text="Buscar archivo", command=leer_csv)
boton.pack()

boton1 = tk.Button(root,text="Motrar Cifrado CESAR", command=lambda:cifradoCesar(palabras))
boton1.pack()

boton2 = tk.Button(root,text="Buscar Cifrado Affine", command=lambda:cifradoAffline(palabras))
boton2.pack()

boton3 = tk.Button(root,text="Buscar Cifrado Mezcla", command=lambda:cifradoMezcla(palabras))
boton3.pack()

frame_rpta = tk.Frame(root)
frame_rpta.pack(expand=True, fill=tk.BOTH)
scrollbar_rpta_y = tk.Scrollbar(frame_rpta, orient=tk.VERTICAL)
scrollbar_rpta_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
mostrarRpta = tk.Text(frame_rpta, height=15, width=25, wrap=tk.NONE, yscrollcommand=scrollbar_rpta_y.set, xscrollcommand=scrollbar_rpta_x.set)
scrollbar_rpta_y.config(command=mostrarRpta.yview)
scrollbar_rpta_x.config(command=mostrarRpta.xview)
mostrarRpta.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
scrollbar_rpta_y.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_rpta_x.pack(side=tk.BOTTOM, fill=tk.X)


frame_encrypt = tk.Frame(root)
frame_encrypt.pack(expand=True, fill=tk.BOTH)
scrollbar_encrypt_y = tk.Scrollbar(frame_encrypt, orient=tk.VERTICAL)
scrollbar_encrypt_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
mostrarEncrypt = tk.Text(frame_encrypt, height=15, width=50, wrap=tk.NONE, yscrollcommand=scrollbar_encrypt_y.set, xscrollcommand=scrollbar_encrypt_x.set)
scrollbar_encrypt_y.config(command=mostrarEncrypt.yview)
scrollbar_encrypt_x.config(command=mostrarEncrypt.xview)
mostrarEncrypt.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
scrollbar_encrypt_y.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar_encrypt_x.pack(side=tk.BOTTOM, fill=tk.X)


root.mainloop() #El mainloop sirve para mantener abierta la ventana y actualizar lo que ocurra dentro de esta