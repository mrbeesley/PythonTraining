#name = input('Enter you name: ')
#print(name)

size_input = input('How big is your house (in square feet): ')
square_feet = int(size_input)
square_meters = square_feet / 10.8
print(f'size in square meeters {square_meters: .2f}')