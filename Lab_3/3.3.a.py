x = ''
lA = []

while True:
    x = input('Type any number or press x to stop and check highest and lowest: ')
    if x != 'x' and '.' not in x:
        lA.append(int(x))
    elif x != 'x' and '.' in x:
        lA.append(float(x))
    elif x == 'x':
        print('---------------------------------------------- \nYour list of numbers is: ', lA)
        break

print('The lowest number is: ', min(lA))
print('The highest number is: ', max(lA))

# 3.3.c.a If anything other than a number is entered, the above lines 7 and 9 will be unable to convert the
# inputs to floats/integers and will present an error. In theory max() and min() can equate strings based
# on the inherent values of the symbols entered.
