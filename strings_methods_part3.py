# ---------------------------
# ---- Strings Methods ------
# ---------------------------

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P")) # Index Number 7
print(a.index("P", 0, 10)) # Index Number 7
# print(a.index("P", 0, 5)) # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(a.find("P")) # Index Number 7
print(a.find("P", 0, 10)) # Index Number 7
print(a.find("P", 0, 5)) # -1

# rjust(width, fill char) ljust(width, fill char)

c = "Mohamed"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Mohamed"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle()) # True
print(two.istitle()) # False

three = " "
four = ""
print(three.isspace()) # True
print(four.isspace()) # False

five = 'i love python'
six = 'I Love Python'
print(five.islower()) # True
print(six.islower()) # False

seven = "mohamed_montaser"
eight = "MohamedMontaser100"
nine = "Mohamed--Montaser100"

print(seven.isidentifier()) # True
print(eight.isidentifier()) # True
print(nine.isidentifier()) # False

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum()) # True
print(z.isalnum()) # True
