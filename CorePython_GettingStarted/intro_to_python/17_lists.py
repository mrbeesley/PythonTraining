
# negative indexing
r = [1, -4, 10, -16, 15]
print(f'r[-1] = {r[-1]}')
print(f'r[-2] = {r[-2]}')
print(f'r[len(r)-1] = {r[len(r)-1]}')


#slicing
s = [3, 186, 4431, 74400, 1048443]
print('s = [3, 186, 4431, 74400, 1048443]')
print(f's[1:3] = {s[1:3]}')
print(f's[1:-1] = {s[1:-1]}')
print(f's[2:] = {s[2:]}')
print(f's[:2] = {s[:2]}')

# using a slice to copy a list
r = s[:]
t = s
print('t = s')
print(f't is s: {t is s}')
print(f't == s: {t == s}')
print('r = s[:]')
print(f'r is s: {r is s}')
print(f'r == s: {r == s}')

# using copy method to copy a list
u = s.copy()
v = list(s)


# dangers of using a slice copy
a = [[1,2], [3,4]]
b = a[:]
print('a = [[1,2], [3,4]]')
print('b = a[:]')
print(f'a is b: {a is b}')
print(f'a == b: {a == b}')
print(f'a[0] = {a[0]}')
print(f'b[0] = {b[0]}')
print(f'a[0] is b[0]: {a[0] is b[0]}')

# using the index method to find elements in a list
w = 'the quick brown fox jumps over the lazy dog'.split()
print(w)
i = w.index('fox')
print("i = w.index('fox')")
print(f'i = {i}')
print("w.count('the'):", w.count('the'))
print('37 in [1, 78,9,37,34,53]', 37 in [1, 78,9,37,34,53])
print('72 in [1, 78,9,37,34,53]', 72 in [1, 78,9,37,34,53])

# remove items from a list
u = "jackdaws love my sphinx of quartz".split()
print(f'u = {u}')
del u[3]
print('del u[3]')
print(f'u = {u}')