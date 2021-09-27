#Control Flow
print("<----------If Statements In Python")
if True: 
    print('yes it is true!')

#won't print
if False: 
    print('its false')

if bool("eggs"):
    print('Yes Please!')

if "eggs":
    print("Yes again!")


print("<----------If-Else Statements In Python")
h = 42
print('h = 42')
if h > 50:
    print('greater than 50')
else:
    print('50 or smaller')

#nested if and else
if h > 50: 
    print('greater than 50')
else:
    if h < 20:
        print("less than 20")
    else:
        print('between 20 and 50')

#using elif
#Flatter is easier to read: Zen of Python
if h > 50:
    print('greater than 50')
elif h < 20:
    print('less than 20')
else:
    print('between 20 and 50')
