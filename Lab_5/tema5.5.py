def media(note):
    m = 0
    if note:
        m = round(sum(note) / len(note), 2)
    return m


def media_materie(elev, materia=None):
    if elev in catalog:
        if materia:
            if materia in materii:
                m = media(catalog[elev][materia])
                print('Media elevului', elev, 'la materia', materii[materia], 'este', m)
            else:
                print('Materia nu exista')
        else:
            print('Mediile elevului', elev, 'sunt:')
            for m in catalog[elev]:
                me = media(catalog[elev][m])
                print(materii[m], ':', me)
    else:
        print('Elevul nu se afla in catalog')


materii = {
    'm': 'Matematica',
    'f': 'Fizica',
    'r': 'Limba Romana'
}

catalog = {
    'Popescu Ion': {
        'm': [2, 5, 7],
        'f': [],
        'r': [6, 9, 8],
    },
    'Ionescu Geta':  {
        'r': [6, 3, 8],
        'm': [4, 5],
        'f': [7, 9, 10]
    },
    'Georgescu Gelu': {
        'm': [2, 5, 7, 9],
        'r': [9, 8],
        'f': [6, 9]
    },
    'Radulescu Ioana': {
        'm': [7],
        'f': [],
        'r': [6, 9, 8],
    },
}

media_materie('Radulescu Ioana')
