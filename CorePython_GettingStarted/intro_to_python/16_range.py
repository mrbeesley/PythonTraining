print(range(5))

for i in range(5):
    print(i)

print(list(range(5,10)))
print(list(range(10,15)))
print(list(range(0,10, 2)))

# example of how not to print items in a list - Zen of Python
s = [0,1,4,6,13]
for i in range(len(s)):
    print(s[i])
# always iterate over the object iteself - Zen of Python
for i in s:
    print(i)

# if you need an index use an iterable to enumerate
t = [6, 372, 8862, 148800, 2096886]
for p in enumerate(t): # enumerate with tuple
    print(p)
for i, p in enumerate(t): # enumerate with tuple unpacking
    print(f'i = {i} and p = {p}')

