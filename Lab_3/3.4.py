s = 'În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele.'

# 3.4.a:

sen = str(s.count('.') + s.count('!') + s.count('?'))

print('There are ' + sen + ' sentences.' + '\n')

# 3.4.b:

words = str(len(s.replace('!', '').replace('?', '').replace(',', '').replace(':', '').replace('.', '').split()))

print('And there are ' + words + ' words.' + '\n')

# 3.4.c:

list_a = s.lower().replace('!', '').replace('?', '').replace(',', '').replace(':', '').replace('.', '').split()

print('The list of all words is as follows:')
print(list_a)
