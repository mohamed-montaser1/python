# ---------------------------
# ---- Strings Methods ------
# ---------------------------

# strip() rstrip() lstrip()

a = "        I Love Python     "
print(a.strip()) # Will remove spaces from start and end
print(a.rstrip()) # Will remove spaces from end
print(a.lstrip()) # Will remove spaces from start


a = "########I Love Python#####"
print(a.strip("#")) # Will remove # from start and end
print(a.rstrip("#")) # Will remove # from end
print(a.lstrip("#")) # Will remove # from start

a = "@#@#@#@#I Love Python@#@#@"
print(a.strip("@#")) # Will remove # and @ from start and end
print(a.rstrip("@#")) # Will remove # and @ from end
print(a.lstrip("@#")) # Will remove # and @ from start

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title()) # I Love 2D Graphics And 3G Technology And Python

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize()) # I love 2d graphics and 3g technology and python

# zfill(width) abbreviation for zero fill
# zfill => Pad a numeric string with zeros on the left, to fill a field of the given width.

c, d, e = "1", "11", "111"

print(c.zfill(3)) # will fill start with zeros
print(d.zfill(3)) # will fill start with zeros
print(e.zfill(3)) # will fill start with zeros

# upper()

g = "mohamed"

print(g.upper()) # MOHAMED

# lower()

h = "MOHamed" # mohamed

print(h.lower())