def make_file():
    with open("note.txt", "w") as my_file:
        print("Popescu Ion;2;5;7", file=my_file)
        print("Ionescu Geta;10;7;9;7", file=my_file)
        print("Georgescu Gelu;4;2", file=my_file)
        print("Radulescu Ioana;5;9;6;4;10", file=my_file)
        print("Vasilescu Vasile;7;8;9;10", file=my_file)
        print("Bengescu Hortensia;10;9;8;9", file=my_file)


def averages():
    x = 'Elev'
    y = 'Media'
    z = '-'
    temp = []
    names = []
    grades = []
    av = []
    with open("note.txt", "r") as read_file:
        print(f'{x:<50}{y:>5} \n{z * 55}')
        for line in read_file:
            temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
            for element in temp:
                names = element[0]
                grades = element[1].split(',')
                for num in grades:
                    av.append(int(num))
                mean = round(sum(av)/len(av), 1)
                print(f'{names:<50}{mean:>5}')
                av.clear()
            temp.clear()



def averages2():
    w = 'Nume'
    x = 'Prenume'
    y = 'Media'
    z = '-'
    nota = 'Note'
    temp = []
    names = []
    grades = []
    av = []
    with open("note.txt", "r") as read_file:
        with open("students.txt", "w") as my_file:
            print(f'{w:<25}{x:<25}{y:>5}{nota:^15} \n{z * 65}', file=my_file)
            for line in read_file:
                temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
                for element in temp:
                    names = element[0].split()
                    grades = element[1].split(',')
                    for num in grades:
                        av.append(int(num))
                    mean = round(sum(av)/len(av), 1)
                    if num:
                        count = len(av)
                    print(f'{names[0]:<25}{names[1]:<25}{mean:>5}{count:^15}', file=my_file)
                    av.clear()
                temp.clear()






def make_sorted_dict():
    # extracts data
    z = '-'
    temp = []
    names = []
    grades = []
    av = []
    values = []
    with open("note.txt", "r") as read:
        for line in read:
            temp.append(str(line).replace(";", ":", 1).replace(";", ",").replace("\n", "").split(':'))
            for element in temp:
                names.append(element[0])
                grades = element[1].split(',')
                for num in grades:
                    av.append(int(num))
                mean = round(sum(av) / len(av), 1)
                values.append(mean)
                av.clear()
                temp.clear()

    # creates a dictonary

    dc = dict(zip(names, values))
    sorted_values = sorted(dc.values(), reverse=True)
    sorted_dict = {}

    # sorts the dictionary

    for i in sorted_values:
        for k in dc.keys():
            if dc[k] == i:
                sorted_dict[k] = dc[k]

    # prints to file
    it = 1
    with open("Sorted_by_Grades.txt", "w") as write:
        print(f'{"Premiu":<25}{"Elev":<25}{"Media":>10}\n{z * 60}', file=write)
        for k, v in sorted_dict.items():
            print(f'{it:<25}{k:<25}{v:>10}', file=write)
            it += 1




def media(t: list) -> float:
    """Compute the average of values in the list"""

    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def get_catalog_from_file(file_name: str) -> dict:
    """Reads the catalog from a text file"""

    ca = {}
    with open(file_name, 'r', encoding='utf-8') as catalog_file:
        for line in catalog_file:
            el = line.strip().split(';')
            ca[el[0]] = list(map(int, el[1:]))
    return ca


def get_teze_from_file(file_name: str) -> dict:
    """Reads 'teze' from a file"""

    te = {}
    with open(file_name, 'r') as teze:
        for line in teze:
            el = line.strip().split(';')
            te[el[0]] = int(el[1])
    return te


def create_final_catalog(c: dict, file_name: str):
    """Create the final catalog"""

    n, m, d = 50, 2, 2

    with open(file_name, 'w') as cat_final:
        header = f'{"Nume":{n}} {"Media":{m}}'
        print(header, file=cat_final)
        print('-' * len(header), file=cat_final)

        for el in sorted(c):
            print(f'{el:<{n}} {media(c[el]):>{m}.{d}f}', file=cat_final)


def all_funcs():
    catalog = get_catalog_from_file('note.txt')
    note_teze = get_teze_from_file('teze.txt')
    create_final_catalog(catalog, 'catalog_final.txt')

