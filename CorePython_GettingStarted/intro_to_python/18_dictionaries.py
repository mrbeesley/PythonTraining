names_and_ages = [('alice', 32), ('bob', 48), ('charlie', 28), ('daniel', 33)]
d = dict(names_and_ages)
print(f'd = {d}')
phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo', f='foxtrot')
print(f'phonetic = {phonetic}')
e = d.copy()
f = dict(d)

g = dict(michael=37, adam=36)
e.update(g)
print(f'e ={e}')

colors = dict(aquamarine='#7ffd4', burlywood='#deb887', 
            chartreuse='#7fff00', cornflower='#6495ed', 
            firebrick='#b22222', honeydew='#f0fff0', 
            maroon='#b03060', sienna='#a0522d')

for key in colors:
    print(f'{key} => {colors[key]}')

for value in colors.values():
    print(value)

for key in colors.keys():
    print(key)

for key, value in colors.items():
    print(f'{key} => {value}')

print('aquamarine' in colors)
print('test' not in colors)

m = {'H': [1,2,3], 
    'He': [3,4], 
    'Li': [6,7],
    'Be': [7,9,10],
    'B': [10, 11],
    'C': [11,12,13,14]}
print(f'm = {m}')
m['H'] += [4, 5, 6, 7]
from pprint import pprint as pp
pp(m)