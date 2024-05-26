import os
import tkinter as tk #Se importa tkinter y se le asigna el nombre de TK
from tkinter import filedialog as FileDialog
from tkinter import messagebox as Message
import csv


def leer_csv():
    file_path = FileDialog.askopenfilename(
        title="Selecciona el archivo",
        filetypes=(("Archivos CSV", "*.csv*"),)
        )
    #El punto csv ayuda a filtrar los archivos

    with open(file_path, newline="") as csvfile:
        reader= csv.reader(csvfile)
        palabras = []
        for row in reader:
            palabras.append(row[0])

        contador = 0
        while contador < len(palabras):
            print(palabras[contador])
            mostrarRpta.insert(tk.END,palabras[contador] + "\n")##Solo sirve este codigo lo demás esta de relleno
            print("\n")

            contador = contador + 1


    
    
    print("Prueba de botón")

    



##FALTA MOSTRAR EL TEXTO ORIGINAL
##LUEGO DE ABRIR EL CSV GUARDAR SU CONTENIDO EN UNA VARIABLE
##


def cifradoCesar():
    respuesta = "Imprimir cifrado cesar"
    mostrarRpta.insert(tk.END, respuesta)
    Message.showinfo("Cifrado Cesar", respuesta)##Mostrar el mensaje cifrado mediante un cuadro de dialogo

    print("Sirve el cifrado cesar")
    ##LUEGO DE PRESIONAR EL BOTON QUE LLAMA A LA FUNCIÓN DEBE CREAR UN ARCHIVO CSV  

def cifradoAffline():
    respuesta = "Imprimir cifrado Affine\n"
    mostrarRpta.insert(tk.END, respuesta)
    nuevaVent = tk.Tk()
    nuevaVent.title("Mensaje encriptado Affine")
    nuevaVent.geometry("720x540")
    respuesta = tk.Label(nuevaVent, text="El mensaje encryptado es %s" % respuesta) ##Mostrar mensaje abriendo una una ventana
    respuesta.pack()

    print("Sirve el cifrado Affline")

def cifradoMezcla():
    respuesta = "Imprimir cifrado Mezcla"
    mostrarRpta.insert(tk.END, respuesta)
    print("Sirve el cifrado Mezcla")




root=tk.Tk() 
root.title("Proyecto LP Encriptación")
root.geometry("1080x720") #Se asigna los valores de ancho y largo de la ventana

etiqueta = tk.Label(root, text="Texto de prueba")
etiqueta.pack() #el .pack hace que se muestre la variable en la que se aplicó


boton = tk.Button(root,text="Buscar archivo", command=leer_csv)
boton.pack()

boton1 = tk.Button(root,text="Motrar Cifrado CESAR", command=cifradoCesar)
boton1.pack()

boton2 = tk.Button(root,text="Buscar Cifrado Affline", command=cifradoAffline)
boton2.pack()

boton3 = tk.Button(root,text="Buscar Cifrado Mezcla", command=cifradoMezcla)
boton3.pack()

mostrarRpta= tk.Text(root, height=100, width=100)
mostrarRpta.pack()





root.mainloop() #El mainloop sirve para mantener abierta la ventana y actualizar lo que ocurra dentro de esta