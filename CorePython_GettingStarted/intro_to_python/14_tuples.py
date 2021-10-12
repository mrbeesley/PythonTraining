
# Tuples
t = ('Norway', 4.953, 3)

print('t = ', t)
print('t[0] = ', t[0])
print('t[2] = ', t[2])
print('len(t) = ', len(t))
for item in t:
    print(item)

# concatenate tuples
print(t + (338186.0, 265e9))

# repeat tuples
print(t * 3)

# nested tuples
a = ((220,284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368))
print('a = ', a)
print('a[2][1] = ', a[2][1])

# single element tuple
h = (391) # this doesn't work!
print('h = ', h)
print('type(h) = ', type(h))
k = (391,) # include a trailing comma for a literal tuple
print('k = ', k)
print('type(k) = ', type(k))

def minmax(items):
    return min(items), max(items)

print('minmax([83, 33, 84, 32, 85, 31, 86]) = ', minmax([83, 33, 84, 32, 85, 31, 86]))

# tuple unpacking
lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])
print('lower, upper = minmax([83, 33, 84, 32, 85, 31, 86])')
print('lower = ', lower)
print('upper = ', upper)

(a, (b, (c, d))) = (4, (3, (2, 1)))
print('(a, (b, (c, d))) = (4, (3, (2, 1)))')
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

# tuple swapping
a = 'jelly'
b = 'bean'
print('a = ', a)
print('b = ', b)
a, b = b, a
print('a, b = b, a')
print('a = ', a)
print('b = ', b)

# tuple from a list
print('tuple([561,1105,1729,2465]) = ', tuple([561,1105,1729,2465]))
print('tuple("Carmichael") = ', tuple('Carmichael'))

# in and not in
print('5 in (3,5,17,157,65537) = ', 5 in (3,5,17,157,65537))
print('5 not in (3,5,17,157,65537) = ', 5 not in (3,5,17,157,65537))




