#While Loops
print("<----------While Loops In Python")
c = 5
while c != 0:
    print(c)
    c -= 1

c = 5
while c:
    print(c)
    c -= 1

while True:
    response = input()
    if int(response) % 7 == 0:
        break
    