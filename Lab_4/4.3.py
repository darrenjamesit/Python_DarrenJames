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

my_list = list(d.items())

for i in range(0, len(my_list)):
    for j in range(0, len(my_list) - i - 1):
        if my_list[j][1] < my_list[j + 1][1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

print('The list of students in descending order of grades is as follows:')
for n, m in my_list:
    print(n, ':', m)
