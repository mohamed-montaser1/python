# ------------------
# --- Calculator ---
# ------------------

operations = "+ - / *"

def main():
  while True:
    print(" Calculator ".center(30, "#"))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter The Operation: ")

    if operation not in operations:
      print(f"The available operations: {operations.split()}")
    else:
      if operation == "+":
        sum(num1, num2)
      elif operation == "-":
        subtraction(num1, num2)
      elif operation == "*":
        multiply(num1, num2)
      elif operation == "/":
        division(num1, num2)

def sum(num1, num2):
  print(num1 + num2)

def subtraction(num1, num2):
  print(num1 - num2)

def multiply(num1, num2):
  print(num1 * num2)

def division(num1, num2):
  print(num1 / num2)

main()