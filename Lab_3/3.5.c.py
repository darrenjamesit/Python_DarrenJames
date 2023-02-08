s = 'În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele.'

j = s.lower().replace('!', '').replace('?', '').replace(',', '').replace(':', '').replace('.', '').replace('î', 'i').split()
l = []

for e in j:
    if e not in l:
        l.append(e)
print(l)

k = []
i = 0


for e in l:
    if e > l[i]:
        k.append(e)
    elif e < l[i]:
        k.insert(0, e)
    else:
        k.append(l[0])
    i += 1
print(k)
