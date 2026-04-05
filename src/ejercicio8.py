'''
def cifrar (mensaje, desplazamiento):
    mensaje_cifrado = [chr(ord(c)+desplazamiento) for c in mensaje]
    mensaje_cifrado = "".join(mensaje_cifrado)
    return mensaje_cifrado

def decifrar (mensaje, desplazamiento):
    mensaje_cifrado = [chr(ord(c)-desplazamiento) for c in mensaje]
    mensaje_cifrado = "".join(mensaje_cifrado)
    return mensaje_cifrado


def cifrar_mensaje(mensaje, desplazamiento):
    mensaje_cifrado = cifrar(mensaje, desplazamiento)
    mensaje_decifrado = decifrar(mensaje_cifrado, desplazamiento)
    print(mensaje)
    print(mensaje_cifrado)
    print(mensaje_decifrado)
'''

'''
def cifrado(mensaje, desplazamiento, operacion='cifrado'):
    signo = 1 if operacion == 'cifrado' else -1
    return "".join(chr(ord(c) + signo * desplazamiento) for c in mensaje)
'''

import string

def cifrado (mensaje, desplazamiento, operacion='cifrar'):
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    letters = string.ascii_letters  
    signo = 1 if operacion == 'cifrar' else -1
    mensaje_cifrado = []
    for c in mensaje:
        if c.islower():
            nueva = letters_lower[
                (letters_lower.index(c) + signo * desplazamiento) % 26
            ]
            mensaje_cifrado.append(nueva)

        elif c.isupper():
            nueva = letters_upper[
                (letters_upper.index(c) + signo * desplazamiento) % 26
            ]
            mensaje_cifrado.append(nueva)

        else:
            mensaje_cifrado.append(c)

    return "".join(mensaje_cifrado)

def cifrar_mensaje(mensaje, desplazamiento):
    mensaje_cifrado = cifrado(mensaje, desplazamiento)
    mensaje_decifrado = cifrado(mensaje_cifrado, desplazamiento, operacion='decifrar')
    print(mensaje)
    print(mensaje_cifrado)
    print(mensaje_decifrado)
