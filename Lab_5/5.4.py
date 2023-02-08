
catalog = {
    'Popescu Ion': {
        'm': [2, 5, 7],
        'f': [],
        'r': [6, 9, 8],
    },
    'Ionescu Geta': {
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

lis = []


def average():
    for k, v in catalog.items():
        print(k)
        for key in v:
            if v[key] == []:
                print(key, 0)
                continue
            print(key, round((sum(v[key])/len(v[key])), 2))


average()
