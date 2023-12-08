# -------------------------
# -------- Variables ------
# -------------------------
# Syntax => [variable name] [assignment operator] [value]
#
# Name Convention and Rules
# [1] Can start with (a-z A-Z) Or Underscore
# [2] You can't start with num or special characters
# [3] you can include (0-9) or underscore in the middle or the end of variable name
# [4] you can't include special character in the name at all
# [5] Name is not like name [ case sensitive ]
# -------------------------

name = "my value"
print(Name) # will give an error => NameError: name 'Name' is not defined. Did you mean: 'name'?

company = 'youtube'
print(company) # youtube

# valid variables name
name = "mohamed montaser"
myName = "mohamed montaser"
my_name = "mohamed montaser"
_name = "mohamed montaser"

# invalid variables name
1name = "mohamed montaser"
@name = "mohamed montaser"