def common_elements():
    first_list = list(range(0, 100, 3))
    second_list = list(range(0, 100, 5))
    elements = set(first_list) & set(second_list)

    return elements

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")
