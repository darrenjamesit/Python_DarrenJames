import time

n = int(input('What factorial would you like to calculate? '))
fac = 1
i = 1


if n == 0:
    print('The answer is 1.')
elif n < 0:
    print('Error, negative numbers do not have factorials.')
else:
    while i <= n:
        fac = fac * i
        i += 1
    print('One moment, let me think')
    time.sleep(0.5)
    print('...')
    time.sleep(0.5)
    print('The factorial of', n, 'is', fac)
