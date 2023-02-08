w = 'Nume'
x = 'Prenume'
y = 'Media'
z = '-'
nota = 'Note'
temp = []
names = []
grades = []
av = []


def averages2():
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

if __name__ == '__main__':
    averages2()
