# -------------------
# ---- Math Exam ----
# -------------------
import random

questions_length= int(input("How many question do you want? "))
asked_questions = 1

def main():
  question = question_generator()
  num1 = question[0]
  num2 = question[2]
  operator = question[1]
  answer = input(f"what {num1} {operator} {num2} is? ")

  if answer.isdigit() or is_float(answer):
    check_is_correct(num1, num2, operator, answer)
  else:
    print("Please enter a valid number!")

def is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

def question_generator():
  num1 = int(random.randint(1, 100))
  num2 = int(random.randint(1, 100))
  operations = ['+', '-', '*', '/']
  operator = random.choice(operations)
  return [num1, operator, num2]

def check_is_correct(num1, num2, operator, answer):
  correct_answer = eval(f"{num1}{operator}{num2}")
  correct_answer = "{:.1f}".format(float(correct_answer))
  answer = "{:.1f}".format(float(answer))
  if correct_answer.strip(" ") == answer.strip(" "):
    print("You are correct!")
  else:
    print("Sorry your answer is wrong")
    print(f"Correct answer is: {correct_answer}")

while asked_questions <= questions_length:
  main()
  asked_questions += 1