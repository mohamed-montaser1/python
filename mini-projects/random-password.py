import random
import string

length = int(input("Please Enter The total length of your password: "))
letters_length = int(input("Please Enter The characters length of your password: "))
nums_length = int(input("Please Enter The numbers length of your password: "))
symbols_length = int(input("Please Enter The symbols length of your password: "))

def generate_password():
  letters = string.ascii_letters
  numbers = string.digits
  symbols = string.punctuation

  chars = (
    random.choices(letters, k=letters_length) + 
    random.choices(numbers, k=nums_length) + 
    random.choices(symbols, k=symbols_length)
  )

  random.shuffle(chars)

  password = "".join(chars)
  return password

if length != (letters_length + nums_length + symbols_length):
  print(f"invalid inputs! total length is: {length}, and sum of the rest is: {letters_length + nums_length + symbols_length}")
else:
  print(generate_password())
