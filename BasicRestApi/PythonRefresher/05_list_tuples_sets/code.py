# List
#list and tuples keep the order or items
l = ['bob', 'rolf', 'anne']

# tuple
# cant change values
t = ("bob", "rolf", "anne")

# set
# can't have duplicate elements in a set
s = {"bob", "rolf", "anne"}

print(l)
print(l[0]) # prints bob
l[0] = "smith"
print(l)

l.append("bob")
print(l)

l.remove('smith')
print(l)

l.reverse()
print(l)