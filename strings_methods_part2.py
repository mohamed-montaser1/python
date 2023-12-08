# ---------------------------
# ---- Strings Methods ------
# ---------------------------

# split() rsplit()

a = "I Love Python and PHP"
print(a.split())

b = "I-Love-Python-and-PHP"
print(b.split('-'))

c = "I-Love-Python-and-PHP"
print(b.split('-', 3)) 

d = "I-Love-Python-and-PHP"
print(b.rsplit('-', 3))

# center

e = "Mohamed"
print(e.center(11)) # Spaces
print(e.center(11, "#")) # Hashes
print(e.center(15, "@")) # @

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP")) # 2 PHP words
print(f.count("PHP", 0, 25)) # Only one PHP


# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I")) # True
print(i.startswith("S")) # False
print(i.startswith("P", 7, 12)) # True

# endswith()

j = "I Love Python"
print(j.endswith("I")) # False
print(j.endswith("S")) # False
print(j.endswith("P", 2, 6)) # True

