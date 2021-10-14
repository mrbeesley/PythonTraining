len('dlkjflkadsjfljad;lj')
print('len("dlkjflkadsjfljad;lj") = ', len('dlkjflkadsjfljad;lj'))
print('New + found + land = ', 'New' + 'found' + 'land')
s = 'New'
print('s = "New"')
print('s = ', s)

s += 'found'
print('s += "found"')
print('s = ', s)

s += 'land'
print('s += "land"')
print('s = ', s)

colors = ';'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])
print("colors = ';'.join(['#45ff23', '#2321fa', '#1298a3', '#a32312'])")
print(colors)
print('colors.split(";")')
print(colors.split(';'))
print("''.join(['high', 'way', 'man'])", ''.join(['high', 'way', 'man']))

# partition strings
print("'unforgetable'.partition('forget')")
print('unforgetable'.partition('forget'))

# using partition with tuple unpacking
departure, seperator, arrival = 'London:Edinburgh'.partition(':')
print("departure, seperator, arrival = 'London:Edinburgh'.partition(':')")
print('departure = ', departure)
print('arrival = ', arrival)

origin, _, destination = 'Seattle-Boston'.partition('-')
print("origin, _, destination = 'Seattle-Boston'.partition('-')")
print('origin = ', origin)
print('destination = ', destination)

# string formatting
print('the age of {0} is {1}'.format('Jim', 32))
print("the age of {0} is {1}. {0}'s birthday is on {2}".format('Fred', 24, 'October 31'))
print("reticulating spline {} of {}".format(4, 23))
print("current position {latitude} {longitude}".format(latitude="60N", longitude="5E"))
print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2,23.1,82.2)))
import math
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))
value = 4 * 20
print('the value is {value}'.format(value=value))

# using f string instead of format
value = 4 * 20
print(f'the value is {value}')
import datetime
print(f'the current time is {datetime.datetime.now().isoformat()}.')
print(f'Math constants: pi={math.pi}, e={math.e}')
print(f'Math constants: pi={math.pi:.3f}, e={math.e:.3f}')
