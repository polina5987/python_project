
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
user_operation = int(input("1. +\n2. -\n3. *\n4. /\nSelect operation: "))
if user_operation == 1:
    print("Result: ", first_number + second_number)
elif user_operation == 2:
    print("Result: ", first_number - second_number)
elif user_operation == 3:
    print("Result: ", first_number * second_number)
elif user_operation == 4:
    if second_number == 0:
        print("Error. Division by 0 isn't allowed.")
    else:
        print("Result: ", first_number/second_number)