
catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

catalog2 = catalog.copy()
lis = []


def el_no(name, grade):
    if name not in catalog2.keys():
        print('Error // Name not in database.')
    elif not (0 <= grade <= 10):
        print('Error // Grades are in the range of 0 - 10 only.')
    else:
        lis.append(grade)
        catalog2[name] = catalog2[name] + lis
        for e, f in catalog2.items():
            print(e, f)


name = input('Type the name of a student: ')
grade = int(input('What grade would you like to add? '))

el_no(name, grade)
