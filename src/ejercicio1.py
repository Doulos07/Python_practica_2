def cantidad_lineas(text):
    return len(text.split('.'))

def cantidad_palabras (text):
    return len(text.split())

def promedio_palabras(text):
    return round(cantidad_palabras(text) / cantidad_lineas(text), 2) 

def encima_promedio(text):
    lineas = text.split('.')
    return [linea for linea in lineas if len(linea.split()) > int(promedio_palabras(text))]