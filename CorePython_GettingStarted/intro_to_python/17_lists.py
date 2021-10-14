
# negative indexing
r = [1, -4, 10, -16, 15]
print(f'r = {r}')
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
u.remove('jackdaws')
print("u.remove('jackdaws')")
print(f'u = {u}')

# insert items into a list
a = 'I accidentally the whole universe'.split()
print(f'a = {a}')
a.insert(2, 'destroyed')
print("a.insert(2, 'destroyed')")
print(f'a = {a}')

# adding concatenating and extending lists
m = [2, 1, 3]
n = [4, 7, 11]
print(f'm = {m}')
print(f'n = {n}')
k = m + n
print('k = m + n')
print(f'k = {k}')
k += [18, 29, 47]
print('k += [18, 29, 47]')
print(f'k = {k}')
k.extend([76, 129, 199])
print('k.extend([76, 129, 199])')
print(f'k = {k}')

# list.reverse and list.sort
g = [1, 11, 21]
print(f'g = {g}')
print('g.reverse()')
g.reverse()
print(f'g = {g}')

d = [17, 29, 41]
print(f'd = {d}')
d.sort()
print('d.sort()')
print(f'd = {d}')
d.sort(reverse=True)
print('d.sort(reverse=True)')
print(f'd = {d}')

# sort by key, or callable item
h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print(f'h = {h}')
h.sort(key=len)
print('h.sort(key=len)')
print(f'h = {h}')
a = ' '.join(h)
print("a = ' '.join(h)")
print(f'a = {a}')

# sorted and reversed
x = [4, 9, 2, 1]
y = sorted(x)
p = [9, 3, 1, 0]
q = reversed(p)
list(q)