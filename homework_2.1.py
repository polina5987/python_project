#version 1
user_number = int(input("Enter your 4-digit number: "))
first_number = user_number // 1000
second_number = user_number % 1000 // 100
third_number = user_number % 1000 % 100 // 10
fourth_number = user_number % 1000 % 100 % 10
print(first_number)
print(second_number)
print(third_number)
print(fourth_number)

# version 2
# user_number = int(input("Enter your 4-digit number: "))
# div, mod = divmod(user_number, 1000)
# div1, mod1 = divmod(mod, 100)
# div2, mod2 = divmod(mod1, 10)
# print(div, div1, div2, mod2, sep="\n")