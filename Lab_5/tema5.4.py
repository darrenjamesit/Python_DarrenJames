def media(note):
    m = 0
    if note:
        m = round(sum(note) / len(note), 2)
    return m


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

mg = 0
for e in catalog:
    mg += media(catalog[e])

mg /= len(catalog)
print('Media generala a clasei este', mg)

