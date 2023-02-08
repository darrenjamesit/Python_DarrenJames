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

for e in d:
    x = round((sum(d[e]))/(len(d[e])), 2)
    d[e] = x

d2 = {}

for f in d:
    if d[f] < 5:
        d2[f] = d[f]

for g in d2:
    print('The student', g, 'has failed with a grade of: ', d2[g])
