def main():
  user_input = input("Enter your sentence you want to reverse here? ")
  if len(user_input.strip("")) == 0:
    print("Please enter a sentence!")
  else:
    reversed_string = reverse_string(user_input)
    print(f"Reversed sentence is: {reversed_string}")


def reverse_string(user_input):
  input_list = list(user_input)
  input_list.reverse()

  result = "".join(input_list)
  return result
main()