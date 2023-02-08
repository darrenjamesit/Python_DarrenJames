catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

w, x, y, z, nota, dash = 'Nume', 'Prenume', 'Media', '-', 'Note', '|'


def average():
    print(f'{z * 65}\n{dash}{w:<25}{x:<25}{y:>5}{nota:^15}{dash}\n{dash}{z * 65}{dash}')
    for key, value in catalog.items():
        lis_surname = key.split()[0]
        lis_firstname = key.split()[1]
        av = round(sum(value)/len(value), 2)
        num = len(value)
        print(f'{dash}{lis_surname:<25}{lis_firstname:<25}{av:>.2f}{num:^15}{dash}')
    print(f'{z * 65}')


average()
