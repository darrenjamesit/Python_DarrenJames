xyz = input('Insert random characters: ')
lista = []

for e in xyz:
    lista.insert(0, e)
    if e == 'x':
        break
print(lista)
