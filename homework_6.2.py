# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59


user_number = int(input("Enter your number: "))
if user_number > 8640000 or user_number < 0:
    print(f"Error! Number {user_number} is not in range")
else:
    days = user_number // 86400
    hours = user_number % 86400 // 3600
    minutes = user_number % 86400 % 3600 // 60
    seconds = user_number % 86400 % 3600 % 60

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (11 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"
        print(f"{days} {day_word} {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")