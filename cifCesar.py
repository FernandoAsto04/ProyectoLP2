import string

alfabeto = list(string.ascii_lowercase)
####Código del cifrado cesar hecha con funciones de alto orden y lambda
def desplazar_letra(letra, desplazamiento):
    if letra in alfabeto:
        indice_actual = alfabeto.index(letra)
        nuevo_indice = (indice_actual + desplazamiento) % len(alfabeto)
        return alfabeto[nuevo_indice]
    else:
        return letra

def cifrar_cesar(arreglo, desplazamiento):
    palabras = " ".join(arreglo)
    mensaje_cifrado = map(lambda letra: desplazar_letra(letra, desplazamiento), palabras)
    return ''.join(mensaje_cifrado)