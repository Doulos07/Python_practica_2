from datos import text
import string


def cantidad_lineas():
    return len(text.split('.'))

def cantidad_palabras ():
    return len(text.split())

def promedio_palabras():
    return round(cantidad_palabras() / cantidad_lineas(), 2) 

def encima_promedio():
    lineas = text.split('.')
    return [linea for linea in lineas if len(linea.split()) > int(promedio_palabras())]