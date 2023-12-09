name = "mohamed montaser"
age = "15"
country = "Egypt"

print("Hello '" + name + "', How You Doing \\ \"\"\" Your Age Is \"" + age + "\" + And Your Country Is: Egypt")
print("Hello '" + name + "', How You Doing \\\n\"\"\" Your Age Is \"" + age + "\" +\nAnd Your Country Is: Egypt")

name = "Elzero"
print('Second Letter is "' + name[1] + '"')
print('Third Letter Is "' + name[2] + '"')
print('Last Letter Is "' + name[-1] + '"')

print(name[1:4])
print(name[0::2])
print(name[-2::-2])

name = "#@#@Mohamed#@#@"
print(name.strip("#@"))

num_one = "9"
num_two = "15"
num_three = "130"
num_four = "950"
num_five = "1500"

print(num_one.zfill(4))
print(num_two.zfill(4))
print(num_three.zfill(4))
print(num_four.zfill(4))
print(num_five.zfill(4))

name_one = "Mohamed"
name_two = "Mohamed_Montaser"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))

name_one = "MOhaMed"
name_two = "moHAmED"

print(name_one.swapcase())
print(name_two.swapcase())

msg = "I Love Python And Although Love Mohamed Montaser"

print(msg.count("Love"))

name = "Elzero"
print(name.find("z"))

msg = "I <3 Python And Although <3 Mohamed Montaser"
print(msg.replace("<3", "Love", 1))
print(msg.replace("<3", "Love"))

name = "mohamed montaser"
age = "15"
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")