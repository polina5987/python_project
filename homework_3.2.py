# version 1
# first_list = [12, 3, 4, 10, 8]
# if first_list:
#     result = first_list[0:-1]
#     result.insert(0, first_list[-1])
#     print(result)
# else: print("Can't change the numbers, list is empty.")

# version 2
first_list = []
if first_list:
    first_list.insert(0, first_list[-1])
    first_list.pop()
    print(first_list)
else: print("Can't change the numbers, list is empty.")
