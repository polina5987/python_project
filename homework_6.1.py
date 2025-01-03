# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

user_letters = input("Enter 2 letters: ")
first_letter, second_letter = user_letters.split("-")
all_symbols = string.ascii_letters

first_index = all_symbols.find(first_letter)
second_index = all_symbols.find(second_letter)

print(all_symbols[first_index:second_index + 1])
