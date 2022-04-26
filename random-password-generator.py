#python3
import random, string

len_number = int(input("Enter your password length : "))
list_number = string.digits

for number in range(len_number):
    if number+1 == len_number:
        print(random.choice(list_number))
    else:
        print(random.choice(list_number), end="")