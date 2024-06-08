import string
from math import gcd

alfabeto = list(string.ascii_lowercase)
m = len(alfabeto)

def letra_a_numero(letra):
    return alfabeto.index(letra)

def numero_a_letra(numero):
    return alfabeto[numero]

def es_coprimo(a, b):
    return gcd(a, b) == 1

def cifrado_affine(letra, a, b):
    if letra in alfabeto:
        x = letra_a_numero(letra)
        y = (a * x + b) % m
        return numero_a_letra(y)
    else:
        return letra

def cifrar_affine(mensaje, a, b):
    if not es_coprimo(a, m):
        raise ValueError(f"{a} y {m} no son coprimos, elige un 'a' diferente.")
    mensaje_cifrado = map(lambda letra: cifrado_affine(letra, a, b), mensaje)
    return ''.join(mensaje_cifrado)
