def second_index(text, some_str):
    index_first = text.find(some_str)

    if index_first == -1:
        return None

    index_second = text.find(some_str, index_first + len(some_str))

    if index_second == -1:
        return None

    return index_second

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
