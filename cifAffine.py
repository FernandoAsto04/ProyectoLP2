import string
from math import gcd

alfabeto = list(string.ascii_lowercase)

def cifrado_affine(letra, a, b):
   return alfabeto[(a * alfabeto.index(letra) + b) % len(alfabeto)]

def cifrar_affine(mensaje, a, b):
    mensaje_cifrado = map(lambda letra: cifrado_affine(letra, a, b), mensaje)
    return ''.join(mensaje_cifrado)
