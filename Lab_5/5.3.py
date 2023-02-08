catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

catalog2 = catalog.copy()
lis = []


def el_no(name, grade=None):
    if name not in catalog2.keys():
        print('Error // Name not in database.')
    elif grade is int and (0 > grade or grade > 10):
        print('Error // Grades are in the range of 0 - 10 only.')
    elif grade is not None and grade not in catalog2[name]:
        print("Error // The entered grade does not correspond with any of this student's grades.")
    else:
        if grade is not None and grade in catalog2[name]:
            for e in catalog2[name]:
                if e != grade:
                    lis.append(e)
            catalog2[name] = lis
        elif grade is None:
            catalog2[name].clear()
        for e, f in catalog2.items():
            print(e, f)


name=input('Type the name of a student: ')
grade=eval(input('What grade would you like to delete? '))
el_no(name, grade)
