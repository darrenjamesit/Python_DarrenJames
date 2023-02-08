x = 'Elev'
y = 'Media'
z = '-'
temp = []
names = []
grades = []
av = []


def averages():
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


if __name__ == '__main__':
    averages()
