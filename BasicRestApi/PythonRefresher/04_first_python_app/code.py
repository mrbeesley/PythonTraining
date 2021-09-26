name = input('What is your name: ')
years = int(input('What is your current age in years: '))
months = years * 12
days = years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f'{name}, you are {years} years old!')
print(f'{name}, you are {months} months old!')
print(f'{name}, you are {days} days old!')
print(f'{name}, you are {hours} hours old!')
print(f'{name}, you are {minutes} minutes old!')
print(f'{name}, you are {seconds} seconds old!')