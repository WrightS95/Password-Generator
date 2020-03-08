#asks how many letters they want in their password
#asks how many numbers
#asks how many special characters
#chooses from lists at random and displays a password with those desired traits

import random
num_of_letters = input("How many letters would you like in your password? ")
num_of_numbers = input("How many numbers would you like in your password? ")
num_of_spec_char = input("How many special characters would you like in your password? ")

letters_password = []
numbers_password = []
spec_password = []

letter_options = "abcdefghijklmnopqrstuvwxyz"
num_options = "1234567890"
spec_options = "!@#$%^&*()[]{};:'/?.>,<`~"

for number in range(int(num_of_letters)):
    letters_password.append(random.choice(letter_options))
for number in range(int(num_of_numbers)):
    numbers_password.append(random.choice(num_options))
for number in range(int(num_of_spec_char)):
    spec_password.append(random.choice(spec_options))

password = []

numbers = int(num_of_numbers)
letters = int(num_of_letters)
spec_char = int(num_of_spec_char)
new_list = letters_password + numbers_password + spec_password
total = numbers + letters + spec_char

for index in range(total):
    chooser = random.choice(new_list)
    password.append(chooser)
    new_list.pop(new_list.index(chooser))
    total -= 1
print(''.join(password))

