def square(x):
    return x * x


print(square(10))


def launch_missiles():
    print('Missiles launched!')


launch_missiles()


def even_or_odd(n):
    if n % 2 == 0:
        print('Even')
        return
    print('Odd')


w = even_or_odd(31)
print(w is None)


def nth_root(radicand, n):
    return radicand ** (1/n)


print(nth_root(16,2))
print(nth_root(27,3))


# function composition
def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'


def ordinal(value):
    return str(value) + ordinal_suffix(value)


def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = 'The ' + ordinal(n) + ' root of ' \
        + str(radicand) + ' is ' + str(root)
    print(message)


display_nth_root(16,2)
display_nth_root(27,3)

# Dunder == Double Underscore, special class functions that can be overwritten 
# __name__ == allows us to detect whether a module is run as a script or imported into another module
