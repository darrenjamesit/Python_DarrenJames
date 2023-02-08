x = ''
lA = []

while True:
    x = input('Type any number or press x to stop and check highest and lowest: ')
    if x != 'x' and '.' not in x:
        lA.append(int(x))
    elif x != 'x' and '.' in x:
        lA.append(float(x))
    elif x == 'x':
        break

print('---------------------------------------------- \nYour list of numbers is: ', lA)

highest = float('-inf')
lowest = float('inf')

for e in lA:
    if e > highest:
        highest = e
    elif e <= highest:
        continue
for e in lA:
    if e < highest:
        lowest = e
    elif e >= highest:
        continue
print('The lowest number is:', lowest)
print('The highest number is:', highest)

# 3.3.c.b This code also doesn't work with anything other than numbers. However assuming the input remained
# as a string, it still wouldn't work as my manual method above compares int+floats but cannot with a string
