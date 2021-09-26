name = 'Bob'
greeting = f'Hello, {name}'

print(greeting)
print(f'Hello, {name}')

name = 'Rolf'
print(greeting)
print(f'Hello, {name}')

name = 'Bob'
greeting = 'Hello, {}'
print(greeting.format(name))

name = 'Rolf'
print(greeting.format(name))

longer_phrase = 'Hello, {}. Today is {}.'

print(longer_phrase.format('Rolf', 'Monday'))