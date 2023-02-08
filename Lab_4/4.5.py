d = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10),
    'Ionescu Temistocle': (2, 9, 4, 10),
    'Popescu Electra': (2, 5, 3),
    'Bengescu Hortensia': (9,),
    'Popescu Sandokan': (7, 6, 7),
}

surnames = []
unique_surnames = []

for e in d:
    surnames.append(e.split()[0])

for f in surnames:
    if f not in unique_surnames:
        unique_surnames.append(f)

for g in unique_surnames:
    print('The surname', '"', g, '"', f' appears {surnames.count(g)} time(s)')
