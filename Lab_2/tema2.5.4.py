user_input = input('Type characters here: ')
abc = []
cba = []



for e in user_input:
    abc.append(e)
for e in user_input:
    cba.insert(0, e)

print(cba)

if abc == cba:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')
