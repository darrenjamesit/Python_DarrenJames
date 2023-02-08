listA = ['ABCD', '12', 'w', ':-)']
listB = []

for e in listA[::-1]:
    listB.append(e[::-1])

print(listB)
