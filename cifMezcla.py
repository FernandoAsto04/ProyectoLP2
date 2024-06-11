import string
from cifCesar import *
from cifAffine import *


def cifrar_mezcla(mensaje, desplazamiento, a, b):
    mensaje_cifrado_cesar = cifrar_cesar(mensaje, desplazamiento)
    mensaje_cifrado_mezcla = cifrar_affine(mensaje_cifrado_cesar, a, b)
    return mensaje_cifrado_mezcla
