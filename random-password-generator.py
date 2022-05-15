#python3
import random, string

char_finally = ""
len_number = int(input("Enter your password length : "))

use_number = string.digits if input("use number ? (Y, N): ") in "yY" else ""

use_lowercase_alphabet = string.ascii_lowercase if input("use lowercase alphabet? (Y, N): ") in "yY" else ""
use_uppercase_alphabet = string.ascii_uppercase if input("use uppercase alphabet? (Y, N): ") in "yY" else ""

use_symbols = string.punctuation if input("use symbols? (Y, N): ") in "yY" else ""

char_finally += use_number + use_lowercase_alphabet + use_uppercase_alphabet + use_symbols

for number in range(len_number):
    if number+1 == len_number:
        print(random.choice(char_finally))
    else:
        print(random.choice(char_finally), end="")