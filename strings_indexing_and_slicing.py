# -------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# -------------------------

# Indexing ( Access Single Item )
myString = "I Love Python"
print(myString[0])
print(myString[9])
print(myString[-1]) # Index -1 => First Character From End
print(myString[-6])

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11]) # yth
print(myString[3:5]) # ov

print(myString[:10]) # If You Didn't Set Start Value It Will be 0 (I Love Pyt)
print(myString[5:])  # If You Didn't Set End Value It Will be str length (e Python)

print(myString[:]) # Full String

print(myString[0::1]) # Full String
print(myString[::1]) # Full String

print(myString[::2]) # ILv yh
print(myString[::3]) # Io t