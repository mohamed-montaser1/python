# ---------------------------
# ---- Strings Formatting ---
# ---------------------------

name = "Mohamed"
age = 15
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age) # Type Error => can only concatenate str (not "int") to str

# %s => string
# %d => digit
# %f => floating point number

print("My name is: %s" % "Mohamed")
print("My name is: %s" % name)
print("My name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

n = "Mohamed"
l = "Python"
y = 10

print("My Name Is %s Iam %s Developer With %d years of Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %.2f" % myNumber)

# Truncate String

myLongString = "Hello Peoples of my community so much"
print("Message is %s" % myLongString) # Message is Hello Peoples of my community so much
print("Message is %.5s" % myLongString) # Message is Hello
