# [1, 3, 5] => 30
# [6] => 36
# [] => 0


numbers = []
new_list = 0
if len(numbers) > 0:
    for i in range(0, len(numbers), 2):
        new_list = new_list + numbers[i]
    result = new_list * max(numbers)

else:
    result = 0

print(result)