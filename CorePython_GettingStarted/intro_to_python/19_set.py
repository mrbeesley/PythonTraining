# elements in a set are immutable
p = {6, 28, 496, 8128, 33550336}
print(f'p = {p}')
print(type(p))
e = set()

# a common use for a set is to remove duplicate items from a list
s = set([2, 4, 16, 64, 4096, 65536, 4, 262144, 16])
print('s = set([2, 4, 16, 64, 4096, 65536, 4, 262144, 16])')
print(f's = {s}')
t = [1, 4, 2, 1, 7, 9, 9]
print(f't = {t}')
print(f'set(t) = {set(t)}')

print('Iterate a set')
print('for x in s:')
for x in s:
    print(f'    {x}')

print(f'1 in s: {1 in s}')
print(f'3 in s: {3 in s}')
print(f'1 not in s: {1 not in s}')

k = {81, 108}
print(f'k = {k}')
k.add(54)
k.add(12)
k.add(108)
k.update([37, 128, 54, 97])
print('k.add(54)')
print('k.add(12)')
print('k.update([37, 128, 54, 97])')
print(f'k = {k}')

k.remove(97)
# discard doesn't though a key error if it can't find the item to remove
k.discard(98)
k.discard(37)
print('k.remove(97)')
print('k.discard(98)')
print('k.discard(37)')
print(f'k = {k}')

# shallow copy works the same as other collections
j = k.copy()

# set algebra
blue_eyes = {'olivia', 'harry', 'lily', 'jack', 'amelia'}
blond_hair = {'harry', 'jack', 'amelia', 'mia', 'joshua'}
smell_hcn = {'harry', 'amelia'}
taste_ptc = {'harry', 'lily', 'amelia', 'lola'}
o_blood = {'mia', 'joshua', 'lily', 'olivia'}
b_blood = {'amelia', 'jack'}
a_blood = {'harry'}
ab_blood = {'joshua', 'lola'}
print(f'blue_eyes = {blue_eyes}')
print(f'blond_hair = {blond_hair}')
print(f'smell_hcn = {smell_hcn}')
print(f'taste_ptc = {taste_ptc}')
print(f'o_blood = {o_blood}')
print(f'b_blood = {b_blood}')
print(f'a_blood = {a_blood}')
print(f'ab_blood = {ab_blood}')
print(f'Bond Hair or Blue Eyes: {blue_eyes.union(blond_hair)}')
print(f'blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes: {blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)}')
print(f'Bond Hair and Blue Eyes: {blue_eyes.intersection(blond_hair)}')
print(f'Bond Hair and not Blue Eyes: {blond_hair.difference(blue_eyes)}')
print(f"smell_hcn.issubset(blond_hair): {smell_hcn.issubset(blond_hair)}")
print(f"taste_ptc.issuperset(smell_hcn): {taste_ptc.issuperset(smell_hcn)}")
print(f'a_blood.isdisjoint(o_blood): {a_blood.isdisjoint(o_blood)}')
