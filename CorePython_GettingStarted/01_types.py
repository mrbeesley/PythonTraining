# Scalar Types

#int 
# - are signed and have unlimited precision based on memory of machine
# - rounding is always toward 0
print("<----------Ints In Python")
print('10:', 10)
print('0b10:', 0b10)
print('0o10:', 0o10)
print('0x10:', 0x10)
print('int(3.5):', int(3.5))
print('int(-3.5):', int(-3.5))
print('int("496"):', int("496"))
print('int("10000", 3):', int("10000", 3))

#float
# - Floating point numbers
# - any operation wtih ints and floats result in float
print("<----------Floats In Python")
print("3.125:", 3.125)
print("3e8:", 3e8)
print("1.616e-35:", 1.616e-35)
print("float(7):", float(7))
print('float("1.618"):', float("1.618"))
print('float("nan"):', float("nan"))
print('float("inf"):', float("inf"))
print('float("-inf"):', float("-inf"))
print("3.0 + 1:", 3.0 + 1)

#null
print("<----------Nulls In Python")
a = None
print(a)
print(a is None)

#bool
print("<----------Bools In Python")
print("True:", True)
print("False:", False)
print("bool(0):", bool(0))
print("bool(42):", bool(42))
print("bool(-1):", bool(-1))
print("bool(0.0):", bool(0.0))
print("bool(0.207):", bool(0.207))
print("bool(-1.117):", bool(-1.117))
print('bool([]):', bool([]))
print('bool([1, 5, 0]):', bool([1, 5, 0]))
print('bool(""):', bool(""))
print('bool("spam"):', bool("spam"))
print('bool("True"):', bool("True"))
print('bool("False"):', bool("False"))
