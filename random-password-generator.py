#python3
import random, string

char_finally = ""
len_number = int(input("Enter your password length : "))

use_number = string.digits if input("use number ? (Y, N): ") in "yY" else ""

use_lowercase_alphabet = string.ascii_lowercase if input("use lowercase alphabet? (Y, N): ") in "yY" else ""
use_uppercase_alphabet = string.ascii_uppercase if input("use uppercase alphabet? (Y, N): ") in "yY" else ""

use_symbols = string.punctuation if input("use symbols? (Y, N): ") in "yY" else ""

char_finally += use_number + use_lowercase_alphabet + use_uppercase_alphabet + use_symbols


while True:
    use_add = input("are you need add char in char list ('show' show list char, Y, N) : ")
    if use_add in "Yy":
        char_finally += input("enter your chars or symbols : ")
        break
    if use_add.lower() == "show":
        print(char_finally)
        continue
    else:
        break


for number in range(len_number):
    if number+1 == len_number:
        print(random.choice(char_finally))
    else:
        print(random.choice(char_finally), end="")
print(char_finally)