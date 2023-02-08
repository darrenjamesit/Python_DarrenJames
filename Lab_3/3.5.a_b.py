s = 'În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele.'

# 3.5.a

j = s.lower().replace('!', '').replace('?', '').replace(',', '').replace(':', '').replace('.', '').split()
l = []

for e in j:
    if e not in l:
        l.append(e)
print(l)

# 3.5.b

l.sort()

print(l)