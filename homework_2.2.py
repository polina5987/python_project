# version 1
# user_number = int(input("Enter you 5-digit number: "))
# number1 = user_number // 10000
# number2 = user_number % 10000 // 1000
# number3 = user_number % 1000 // 100
# number4 = user_number % 100 // 10
# number5 = user_number % 10000 % 1000 % 100 % 100 % 10
# print(f"{number5}{number4}{number3}{number2}{number1}")

# version 2
user_number = int(input("Enter you 5-digit number: "))
number1 = user_number // 10000
number2 = user_number % 10000 // 1000
number3 = user_number % 1000 // 100
number4 = user_number % 100 // 10
number5 = user_number % 10000 % 1000 % 100 % 100 % 10
result = number1 + number2 * 10 + number3 * 100 + number4 * 1000 + number5 * 10000
print(result)