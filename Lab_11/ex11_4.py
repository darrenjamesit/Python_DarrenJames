import os
import time

start = time.process_time_ns()

files = []
total_size = []
path = "C:/Users/Darren James/Documents/Coding/PYTHON/Lab_11"

for root, dir, file in os.walk(path):
    for filename in file:
        size = os.path.getsize(os.path.join(root, filename))
        total_size.append(size)

end = time.process_time_ns()

print('Start dir: ', path)
print(f'Total file size: {round(sum(total_size)/1024, 3)} kB')
print('-----------------------------')
print(f"Total process time: {(end - start)/1000000} milliseconds")