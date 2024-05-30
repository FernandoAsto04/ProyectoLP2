import string
from math import gcd

alfabeto = list(string.ascii_lowercase)
m = len(alfabeto)

def desplazar_letra(letra, desplazamiento):
    if letra in alfabeto:
        indice_actual = alfabeto.index(letra)
        nuevo_indice = (indice_actual + desplazamiento) % m
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

def cifrar_mezcla(mensaje, desplazamiento_cesar, a, b):
    mensaje_cifrado_cesar = cifrar_cesar(mensaje, desplazamiento_cesar)
    mensaje_cifrado_mezcla = cifrar_affine(mensaje_cifrado_cesar, a, b)
    return mensaje_cifrado_mezcla

# Prueba de la función
mensaje = "hola mundo"
desplazamiento_cesar = 3
a = 23
b = 5

mensaje_cifrado_mezcla = cifrar_mezcla(mensaje, desplazamiento_cesar, a, b)
print(mensaje_cifrado_mezcla)  # La salida será un mensaje cifrado
