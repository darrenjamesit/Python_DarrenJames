import os

dirs = []
files = []
path = "C:/Users/Darren James/Documents/Coding/PYTHON"

for root, dir, file in os.walk(path):
    dirs.extend(dir)
    files.extend(file)

dircount = len(dirs)
filecount = len(files)

print(path)
print('Nr. of Folders: ', dircount)
print('Nr. of Files: ', filecount)