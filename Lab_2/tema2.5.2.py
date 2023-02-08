print('Please choose 3 values for the sides of a triangle:')

a = int(input('Length of side A: '))
b = int(input('Length of side B: '))
c = int(input('Length of side C: '))
d = a ** 2
e = b ** 2
f = c ** 2

if a == b == c:
    print('Triunghiul este echilateral.')
elif a == b or b == c or a == c:
    print('Triunghiul este isoscel.')
elif (d + e) == f or (e + f) == d or (d + f) == e:
    print('Triunghiul este dreptunghic.')
else:
    print('Triunghiul este oarecare.')
