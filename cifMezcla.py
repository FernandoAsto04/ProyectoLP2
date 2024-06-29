from cifCesar import *
from cifAffine import *

#Esta función aplica primero el cifrado cesar y luego el cifrado affine, a lo que se retorna la letra calculada luego de aplicar ambos cifrados
def cifrar_mezcla(mensaje, desplazamiento, a, b):
    mensaje_cifrado_cesar = cifrar_cesar(mensaje, desplazamiento)
    mensaje_cifrado_mezcla = cifrar_affine(mensaje_cifrado_cesar, a, b)
    return mensaje_cifrado_mezcla

#Implementado por Fernando Asto