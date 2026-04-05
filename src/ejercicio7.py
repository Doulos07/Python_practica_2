import random

def sorteo_amigo_invisible(personas):
    # Elimino duplicados
    personas = list(set([p.lower().strip() for p in personas]))
    parejas = []
    
    # Validar
    if len(personas)< 3: return []

    mezcla = personas[:]

    while True:
        random.shuffle(mezcla)
        # Valido si Todos(ALL) los elementos complemen la condicion
        if all(m != p for m, p in zip(mezcla, personas)):
            break

    return list(zip(mezcla, personas))

'''
zip()
sirve para Combinar o emparejar
zip, recorre 'en paralelo', generando pares(o tuplas) con elementos de la misma posicion
IMPORTANTE ambas listan tiene que tener la misma longitud
PAR -> devuelve una lista con parejas 
IMPAR -> devuelve todos parejas menos uno 
'''

