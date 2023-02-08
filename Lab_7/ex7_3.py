z = '-'
temp = []
names = []
grades = []
av = []
values = []



def make_sorted_dict():
    # extracts data

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


make_sorted_dict()

