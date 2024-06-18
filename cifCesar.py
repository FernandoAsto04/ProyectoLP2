import string
#Código del cifrado cesar hecho con funciones de alto orden y lambda
#Se crea esta lista para poder acceder facilmente a las letras
alfabeto = list(string.ascii_lowercase)

#Esta función encuentra la posición de una letra en el alfabeto, tras esto calcula la nueva posición y 
#devuelve la letra perteneciente a la nueva posición calculada
def desplazar_letra(letra, desplazamiento):
    return alfabeto[(alfabeto.index(letra)+desplazamiento%len(alfabeto))]

#Esta función recibe un mensaje y desplazamiento los cuales provienen de un archivo csv. La función lamba 
#toma un argumento 'letra' y llama a la función desplazar_letra para aplicarle la función. Mientras que la función 
#map envía cada letra del mensaje para que se pueda cifrar
def cifrar_cesar(mensaje, desplazamiento):
    mensaje_cifrado = map(lambda letra: desplazar_letra(letra, desplazamiento), mensaje)
    return ''.join(mensaje_cifrado)
