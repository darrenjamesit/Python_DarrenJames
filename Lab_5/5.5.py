
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

catalog2 = catalog.copy()
lis = []


def average(name, subject=None):
    if name not in catalog2.keys():
        print('Error // Name not in database.')
    else:
        for k, v in catalog.items():
            if subject is not None and subject in v:
                for subject, values in v:
                    if subject == "m":
                        subject = "Maths"
                    elif subject == "f":
                        subject = "Physics"
                    elif subject == "r":
                        subject = "Romanian"
                    elif v[subject] == []:
                        print("The student ", name, "has an average of", 0, "in ", subject, ".")
                        break
                print(subject, round((sum(v[subject])/len(v[subject])), 2))


average(name=input('Type the name of the student: '), subject=eval(input('type subject "m", "f", "r" or None: ')))

