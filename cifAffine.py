import string

alfabeto = list(string.ascii_lowercase)
print(alfabeto)
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
    palabras = " ".join(mensaje)
    mensaje_cifrado = map(lambda letra: cifrado_affine(letra, a, b), palabras)
    return ''.join(mensaje_cifrado)