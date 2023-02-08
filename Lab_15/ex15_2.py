with open("student.csv", "r") as read:
    first = read.readline()
    next(read)
    with open("tema15_2.txt", "w") as write:
        for line in read:
            p_line = str(line.replace('\n', '').split(',')).replace("[", "").replace("]", "")
            print(f"insert into student ({first}) \nvalues ({p_line});\n", file=write)
