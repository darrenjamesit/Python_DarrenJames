catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

catalog2 = catalog.copy()
lis = []


def el_no_ov(name, grade, overwrite=False):
    if name not in catalog2.keys():
        print('Error // Name not in database.')
    elif 0 > grade or grade > 10:
        print('Error // Grades are in the range of 0 - 10 only.')
    elif overwrite != (True or False):
        print("Error // Overwrite can only be True or Flase.")
    else:
        if overwrite is False:
            lis.append(grade)
            catalog2[name] = catalog2[name] + lis
        elif overwrite is True:
            lis.append(grade)
            catalog2[name] = lis
        for e, f in catalog2.items():
            print(e, f)


el_no_ov(name=input('Type the name of a student: '), grade=int(input('What grade would you like to add? ')), overwrite=eval(input('Type True to replace all grades with entered grade, otherwise type False to add the grade at the end: ')))
