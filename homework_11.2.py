def generate_cube_numbers(end):
    n = 2
    while n ** 3 <= end:
        yield n ** 3
        n += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки 2 в кубі дає 8, що менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 в кубі дає 125, що більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 в кубі дає 1000'

print('Ok')
