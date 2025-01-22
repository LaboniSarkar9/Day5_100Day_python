import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n "))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How mny numbers would you like ?\n "))


#Easy level
password = ""

#nr_letters = 4
# for char in range (1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
#     print(password)
#
# for num in range (1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password += random_num
#     print(password)
#
# for symb in range (1, nr_symbols + 1):
#     random_symbol = random.choice(symb)
#     password += random_symbol
#     print(password)


for char in range (1, nr_letters + 1):
    password += random.choice(letters)


for num in range (1, nr_numbers + 1):
    password += random.choice(numbers)


for symb in range (1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)

