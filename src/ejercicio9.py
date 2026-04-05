def tiene_nombre(name):

    if name is None:
        return False


    name = name.strip()

    if not name: return False

    for c in name:
        if not (c.isalpha() or c == " "): return False

    return True

def tiene_nota(nota):
    if nota is None:
        return False


    nota = nota.strip()

    if not nota: return False

    for c in nota:
        if not c.isdigit(): return False

    return True

def formato_capitalize(text):
    return text.strip().lower().capitalize()

def formatear_estudiante(estudiante):
    estudiante['name'] = formato_capitalize(estudiante['name'])
    estudiante['grade'] = int(estudiante['grade'])
    estudiante['status'] = formato_capitalize(estudiante['status'])

    return estudiante


def filtrar_estudiante(estudiantes):
    filtro = {}
    
    for e in estudiantes:
        nombre = e['name']
        nota = e['grade']

        if nombre not in filtro:
            filtro[nombre] = e
        else:
            if nota > filtro[nombre]['grade']:
                filtro[e['name']] = e
    
    return list(filtro.values())

def normalizar_registro(students):
    filtro_estudiante = []
    for student in students:
        name = student['name']
        # por alguna razon si vuelvo a ejecutar por 2da vez el mismo metodo los datos de grade queda guardo como int en vez de str por eso lo paso a str explicitamente
        nota = str(student['grade'])

        # print(f'nota: {nota}, tipo: {type(nota)}')
        if (tiene_nombre(name) and tiene_nota(nota)):
            filtro_estudiante.append(formatear_estudiante(student))
    
    filtro_estudiante = filtrar_estudiante(filtro_estudiante)
    filtro_estudiante = sorted(filtro_estudiante, key=lambda x: x['name'])

    return filtro_estudiante

