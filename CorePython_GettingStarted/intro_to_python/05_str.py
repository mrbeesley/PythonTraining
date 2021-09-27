# strings in python are immutable

#multiline strings are denoted by 3 quotes instead of one
test_string = '''testing
testing next line
'''
test_quote_string = """testing
testing next line
"""
test_escape_string = 'testing \nTesting next line'


print(test_string)
print(test_quote_string)
print(test_escape_string)


print("This is a \" in a string")
print('This is a \' in a string')
print('This is a " and a \' in a string')
print('a \\ in a string')

path = r'c:\users\merlin\documents\spells'
print(path)
print(str(496))
print(str(6.02e23))
s = 'Parrot'
print(s[4])

c = 'oslo'
print(c.capitalize())
print(c)