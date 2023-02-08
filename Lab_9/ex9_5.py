x = 1

for x in range(1, 4):
    with open(f"premiu-{x}.txt", "w") as write:
        x += 1
while x < 4:
    with open("Sorted_by_Grades.txt", "r") as read:
        with open("model.txt", "r") as model:
            for line in read.readlines()[2:5]:
                grade = line.split()
                y = grade[0]
                name = grade[1] + grade[2]
                average = grade[3]
                with open(f"premiu-{y}.txt", "w") as write_again:
                    for lyn in model:
                        premiu = lyn.replace("premiul {}", f'premiul {y}')
                        nume = lyn.replace("/elevei {}",f'/elevei {name}')
                        media = lyn.replace(": {}", f': {average}')
                        write_again.write(f'{premiu} \n {nume} \n {media}')
    x += 1
