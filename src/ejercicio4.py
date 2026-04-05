def validation_mail (mail):
    invalid = ('.', '@')
    part_mail = mail.split('@')
    dominio = mail.split('.')[-1]

    if not '@' in mail: return 'No contiene el caracter "@"'
    if len(part_mail) < 2: return 'Tiene que contener caracteres antes del "@"'
    if not '.' in part_mail[1]: return 'Tiene que contener un "." despues del "@"'
    if (mail[0] in invalid) or (mail[-1] in invalid): return 'El Mail no puede empezar ni termina con "@" ni con "."'
    if len(dominio) < 2: return 'Dominio invalido'

    return 'Mail valido'