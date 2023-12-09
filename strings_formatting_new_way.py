# ---------------------------
# ---- Strings Formatting ---
# ---------------------------

name = "Mohamed"
age = 15
rank = 10

print("My name is: {}".format("Mohamed"))
print("My name is: {}".format(name))
print("My Name is: {} and My Age is: {}".format(name, age))
print("My Name is: {:s} and My Age is: {:d} and My Rank is: {:f}".format(name, age, rank))

# {:s} => string
# {:d} => digit
# {:f} => floating point number

n = "Mohamed"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of my community so much"
print("Message is {:s}".format(myLongString)) # Message is Hello Peoples of my community so much
print("Message is {:.5s}".format(myLongString)) # Message is Hello
print("Message is {:.13s}".format(myLongString)) # Message is Hello Peoples

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))
# print("My Money in Bank Is: {:&d}".format(myMoney)) # Wrong =>  Invalid format specifier '&d' for object of type 'int

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c)) # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c)) # Hello Two Three One
print("Hello {2} {1} {0}".format(a, b, c)) # Hello Three Two One
print("Hello {2} {0} {1}".format(a, b, c)) # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z)) # Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}".format(x, y, z)) # Hello 20 30 10
print("Hello {2:f} {1:f} {0:f}".format(x, y, z)) # Hello 30.000000 20.000000 10.000000
print("Hello {2:.2f} {0:.4f} {1:.4f}".format(x, y, z)) # Hello 30.00 10.0000 20.0000

# Format in Version 3.6+

myName = "Mohamed"
myAge = 15

print(f"My Name is: {myName} and My Age is: {myAge}")