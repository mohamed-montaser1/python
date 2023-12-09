# -------------------------
# -------- Numbers --------
# -------------------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# FLoat

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))

print(f"Real Part Is: {myComplexNumber.real}")
print(f"Imaginary Part Is: {myComplexNumber.imag}")

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Another Type

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
print(int(10+9j)) # Error => TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'