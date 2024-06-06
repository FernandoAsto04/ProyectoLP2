import string

alfabeto = list(string.ascii_lowercase)

def desplazar_letra(letra, desplazamiento):
    if letra in alfabeto:
        indice_actual = alfabeto.index(letra)
        nuevo_indice = (indice_actual + desplazamiento) % len(alfabeto)
        return alfabeto[nuevo_indice]
    else:
        return letra

def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = map(lambda letra: desplazar_letra(letra, desplazamiento), mensaje)
    return ''.join(mensaje_cifrado)

def letra_a_numero(letra):
    return alfabeto.index(letra)

def numero_a_letra(numero):
    return alfabeto[numero]

def cifrado_affine(letra, a, b):
    if letra in alfabeto:
        x = letra_a_numero(letra)
        y = (a * x + b) % len(alfabeto)
        return numero_a_letra(y)
    else:
        return letra

def cifrar_affine(mensaje, a, b):
    mensaje_cifrado = map(lambda letra: cifrado_affine(letra, a, b), mensaje)
    return ''.join(mensaje_cifrado)

def cifrar_mezcla(mensaje, desplazamiento_cesar, a, b):
    mensaje_cifrado_cesar = cifrar_cesar(mensaje, desplazamiento_cesar)
    mensaje_cifrado_mezcla = cifrar_affine(mensaje_cifrado_cesar, a, b)
    return mensaje_cifrado_mezcla