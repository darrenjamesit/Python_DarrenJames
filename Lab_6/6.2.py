catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

w, x, y, z = 'Nume', 'Prenume', 'Media', '-'


def average():
    print(f'{w:<25}{x:<25}{y:>5} \n{z * 55}')
    for key, value in catalog.items():
        lis_surname = key.split()[0]
        lis_firstname = key.split()[1]
        if value:
            av = round(sum(value)/len(value), 2)
            print(f'{lis_surname:<25}{lis_firstname:<25}{av:>.2f}')
        else:
            print(f'{lis_surname:<25}{lis_firstname:<25}{0:>.2f}')


average()
