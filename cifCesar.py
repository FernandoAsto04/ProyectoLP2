import string
####Código del cifrado cesar hecha con funciones de alto orden y lambda
alfabeto = list(string.ascii_lowercase)

def desplazar_letra(letra, desplazamiento):
    return alfabeto[(alfabeto.index(letra)+desplazamiento%len(alfabeto))]

def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = map(lambda letra: desplazar_letra(letra, desplazamiento), mensaje)
    return ''.join(mensaje_cifrado)
