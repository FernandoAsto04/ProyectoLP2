import string
####Código del cifrado cesar hecha con funciones de alto orden y lambda
alfabeto = list(string.ascii_lowercase)

def desplazar_letra(letra, desplazamiento):
    if letra in alfabeto:
        indice_actual = alfabeto.index(letra)
        nuevo_indice = (indice_actual + desplazamiento) % len(alfabeto)
        return alfabeto[nuevo_indice]
    else:
        return letra

def cifrar_cesar(arreglo, desplazamiento):
    palabras = map(lambda palabra: ''.join(palabra), arreglo)
    mensaje_cifrado = map(lambda letra: desplazar_letra(letra, desplazamiento), palabras)
    return ''.join(mensaje_cifrado)

# Prueba de la función
#mensaje = "hola mundo"
#desplazamiento = 3
#mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
#print(mensaje_cifrado)  # Salida: "krod pxqgr"
