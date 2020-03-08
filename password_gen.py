#asks how many letters they want in their password
#asks how many numbers
#asks how many special characters
#chooses from lists at random and displays a password with those desired traits

import random
max_of_char = int(input("How many characters would you like your password to have? "))
num_of_letters = int(input("How many letters would you like in your password? "))
num_of_numbers = int(input("How many numbers would you like in your password? "))
num_of_spec_char = int(input("How many special characters would you like in your password? "))
total = num_of_numbers+num_of_letters+num_of_spec_char

letters_password = []
numbers_password = []
spec_password = []

letter_options = "abcdefghijklmnopqrstuvwxyz"
num_options = "1234567890"
spec_options = "!@#$%^&*()[]{};:'/?.>,<`~"

for number in range(num_of_letters):
    letters_password.append(random.choice(letter_options))
for number in range(num_of_numbers):
    numbers_password.append(random.choice(num_options))
for number in range(num_of_spec_char):
    spec_password.append(random.choice(spec_options))

password = []
new_list = letters_password + numbers_password + spec_password

for index in range(total):
    chooser = random.choice(new_list)
    password.append(chooser)
if max_of_char < total:
    print("WARNING: The sum of characters is greater than the maximum char")
print(''.join(password))

