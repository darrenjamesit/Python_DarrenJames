lista = []

while True:
    xyz = input('Insert random characters: ')
    if xyz != 'X':
        lista.append(xyz)
    elif xyz == 'X':
        break
print(lista)
