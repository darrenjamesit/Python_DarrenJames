catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

x, y, z = 'Elev', 'Media', '-'


def average():
    print(f'{x:<50}{y:>5} \n{z * 55}')
    for key, value in catalog.items():
        if value:
            av = round(sum(value)/len(value), 2)
            print(f'{key:<50} {av:>.2f}')
        else:
            print(f'{key:<50} {0:>.2f}')


average()
