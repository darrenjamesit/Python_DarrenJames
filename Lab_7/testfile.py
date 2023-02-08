def make_file():
    with open("note.txt", "w") as my_file:
        print("Popescu Ion;2;5;7", file=my_file)
        print("Ionescu Geta;10;7;9;7", file=my_file)
        print("Georgescu Gelu;4;2", file=my_file)
        print("Radulescu Ioana;5;9;6;4;10", file=my_file)
        print("Vasilescu Vasile;7;8;9;10", file=my_file)
        print("Bengescu Hortensia;10;9;8;9", file=my_file)

#
# make_file()
