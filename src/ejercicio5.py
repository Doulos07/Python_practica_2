zonas = {
    'local': [500, 1000, 200],
    'regional': [1000, 2500, 5000],
    'nacional': [2000, 4500, 8000], 
}



def calcular_envio (peso, envio):
    if envio in zonas.keys():
        if peso <= 1:
            index = 0
        else:
            index = 0 if peso > 5 else 1
        return f'Costo del envío: ${zonas[envio][index]}'
    else:
        return 'Zona invalida'