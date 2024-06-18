#Se importan las librerías y archivos necesarios
import tkinter as tk 
from tkinter import filedialog as FileSearch
from tkinter import messagebox as Message
from cifCesar import *
from cifAffine import *
from cifMezcla import *
import csv


palabras=[]
#Esta función abre una ventana de busqueda para seleccionar una archivo csv
def leer_csv():
    file_path = FileSearch.askopenfilename(
        title="Selecciona el archivo",
        filetypes=(("Archivos CSV", "*.csv*"),)
        )

    with open(file_path, newline="") as csvfile:
        reader= csv.reader(csvfile)
        
        for row in reader:
            palabras.append(row[0])

        contador = 0
        while contador < len(palabras):
            print(palabras[contador])
            mostrarRpta.insert(tk.END,palabras[contador] + "\n")
            print("\n")
            contador = contador + 1


def cifradoCesar():
    with open('cifrado_Cesar.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        i=0
        while i < len(palabras):
            desplazamiento = 3
            result = cifrar_cesar(palabras[i], desplazamiento)
            csv_writer.writerow([result])  # Escribe el resultado cifrado en una fila en el archivo CSV 🫡🫡🫡🫡🫡(Mensaje puesto para que cierta persona entienda)
            mostrarEncrypt.insert(tk.END, result)
            mostrarEncrypt.insert(tk.END, "\n")
            i = i + 1


def cifradoAffine():
    with open('cifrado_Affine.csv', 'w',newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        i=0
        while i<len(palabras):
            a=23
            b=5
            result = cifrar_affine(palabras[i],a,b)
            csv_writer.writerow([result])
            mostrarEncrypt.insert(tk.END, result)
            mostrarEncrypt.insert(tk.END, "\n")
            i=i+1


def cifradoMezcla():
    with open('cifrado_Mezcla.csv', 'w',newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        i=0
        while i < len(palabras):
            a=23
            b=5
            desplazamiento = 3
            result = cifrar_mezcla(palabras[i],desplazamiento,a,b)
            csv_writer.writerow([result])
            mostrarEncrypt.insert(tk.END, result)
            mostrarEncrypt.insert(tk.END, "\n")
            i=i+1

#Código de la interfaz, en esta parte está incluido el código orientado a eventos
root=tk.Tk() 
root.title("Proyecto LP Encriptación")
root.geometry("1080x720") #Se asigna los valores de ancho y largo de la ventana

etiqueta = tk.Label(root, text="Texto de prueba")
etiqueta.pack() #el .pack hace que se muestre la variable en la que se aplicó


boton = tk.Button(root,text="Buscar archivo", command=leer_csv)
boton.pack()

boton1 = tk.Button(root,text="Motrar Cifrado Cesar", command=cifradoCesar)
boton1.pack()

boton2 = tk.Button(root,text="Buscar Cifrado Affine", command=cifradoAffine)
boton2.pack()

boton3 = tk.Button(root,text="Buscar Cifrado Mezcla", command=cifradoMezcla)
boton3.pack()

frame_rpta = tk.Frame(root)
frame_rpta.pack(expand=True, fill=tk.BOTH)
scrollbar_rpta_y = tk.Scrollbar(frame_rpta, orient=tk.VERTICAL)
scrollbar_rpta_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
mostrarRpta = tk.Text(frame_rpta, height=15, width=15, wrap=tk.NONE, yscrollcommand=scrollbar_rpta_y.set, xscrollcommand=scrollbar_rpta_x.set)
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