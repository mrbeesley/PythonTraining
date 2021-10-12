count = 0
print('count = ', count)
def show_count():
    print(count)

def set_count(c):
    count = c

print('show_count()')
show_count()
set_count(5)
print('set_count(5)')
print('show_count()')
show_count()

def set_count_global(c):
    global count
    count = c

print('show_count()')
show_count()
set_count_global(5)
print('set_count_global(5)')
print('show_count()')
show_count()