import random
import string

numbers = list(string.digits)

right_guess_msg = "\n\n Your guess is right! \n\n" 
def wrong_guess_msg(guess):
  return f"\n\nSorry your guess is wrong, the right number is: {guess}\n\n"

def main():
  while True:
    random.shuffle(numbers)
    guess = int(random.choice(numbers))
    user_guess = int(input("guess the number between 0-9: "))
    if guess == user_guess:
      print("\n")
      print(right_guess_msg.center(len(right_guess_msg) + 100, "#"))
      print("\n")
      break
    else:
      print("\n")
      print(wrong_guess_msg(guess).center(len(wrong_guess_msg(guess)) + 100, "#"))
      print("\n")

main()