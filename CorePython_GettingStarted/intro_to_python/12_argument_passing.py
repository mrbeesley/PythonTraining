m = [9, 15, 24]
def modify(k):
    k.append(39)
    print('k = ', k)
modify(m)


def replace(g):
    g = [17,28,45]
    print("g = ", g)

replace(m)
print('m = ', m)

# default arguments
def banner(message, border='-'):
    # when you multiply a string by a number gives a new string repeated x times
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner('Norwegian Blue')
banner('Sun, Moon, and Stars', border='*')

# default value evaluation with mutable default value
def add_spam_mutable(menu=[]):
    menu.append("spam")
    return menu

# default value evaluation with immutable default value
def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

breakfast = ['bacon', 'eggs']
print('breakfast = ', breakfast)
print('adding spam to breakfast...', add_spam(breakfast))
lunch = ['baked beans']
print('lunch = ', lunch)
print('adding spam to lunch...', add_spam(lunch))
print('just adding spam 1...', add_spam())
print('just adding spam 2...', add_spam())
print('just adding spam 3...', add_spam())
print('just adding spam 4...', add_spam())

