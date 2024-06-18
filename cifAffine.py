import string
from math import gcd
#Código del cifrado Affine hecho con funciones de alto orden y lambda
alfabeto = list(string.ascii_lowercase)

#Esta función halla la posición de la letra en el alfabeto y luego calcula la nueva posición de la letra usando la fórmula del cifrado Affine.
#Finalmente retorna la letra correspondiente a la nueva poscición calculada.
def cifrado_affine(letra, a, b):
   return alfabeto[(a * alfabeto.index(letra) + b) % len(alfabeto)]

#Esta función recibe un mensaje junto a dos valores, a y b, que por defecto son 23 y 5 respectivamente. La función cifra el mensaje 
#utilizando el cifrado Affine de la siguiente manera: toma el mensaje y aplica la función cifrado_affine a cada letra mediante una 
#función lambda. map envía cada letra del mensaje a la función lambda para que se complete la encriptación de todo el mensaje. 
#Finalmente, las letras cifradas se unen en una sola cadena que se retorna como el mensaje cifrado.
def cifrar_affine(mensaje, a, b):
    mensaje_cifrado = map(lambda letra: cifrado_affine(letra, a, b), mensaje)
    return ''.join(mensaje_cifrado)
