import os

files = []
pyfiles = []
path = "C:/Users/Darren James/Documents/Coding/PYTHON/Lab_11"

for root, dir, file in os.walk(path):
    if file != []:
        files.append(file)

for firstlist in files:
    for filename in firstlist:
        if filename.lower().endswith(".py"):
            pyfiles.append(filename)
            print(filename)

print('Nr. of Python files: ', len(pyfiles))