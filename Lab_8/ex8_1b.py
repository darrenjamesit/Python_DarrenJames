from ex8_1a import *


def choose(x: int):
    if x == 1:
        make_file()
        averages()
    elif x == 2:
        averages2()
    elif x == 3:
        make_sorted_dict()
    elif x == 4:
        all_funcs()
    else:
        print('Invalid selection.')


choose(int(input('''Please choose one of the available options
by typing the corresponding number:
1 -> Exercise 7.1
2 -> Exercise 7.2
3 -> Exercise 7.3
4 -> Exercise 7.4
Please note, options 2-4 will not runn without first running option 1.

Option selected: ''')))
