import random
latter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '\\', '|', '`', '~']
print("Welcome to the PyPassword Generator!")
nr_latter = int(input("How many latters would you like in your password.\n"))
nr_number = int(input("How many numbers would you like in your password.\n"))
nr_symbol = int(input("How many symbols would you like in your password.\n"))

Want = input("You want to make a easy password or hard password. If you want to make easy possword write 'Easy' or If you want to make eassy possword write 'Hard'.\n")
want = Want.lower()
if want == "easy":
  password = " "
  for char in range(1, nr_latter +1):
    password += random.choice(latter)

  for char in range(1, nr_number +1):
    password += random.choice(number)

  for char in range(1, nr_symbol +1):
    password += random.choice(symbol)

  print(f"Your easy password \n{password}")

elif want == "hard":
  password_list = []
  for char in range(1, nr_latter +1):
    password_list.append(random.choice(latter))

  for char in range(1, nr_number +1):
    password_list += random.choice(number)

  for char in range(1, nr_symbol +1):
    password_list += random.choice(symbol)
  random.shuffle(password_list)
  new_password = ""
  for char in password_list:
    new_password += char
  print(f"Your hard password \n{new_password}")
