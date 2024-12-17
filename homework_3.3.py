numbers = []
if len(numbers) % 2 == 0:
    part1 = numbers[0:len(numbers)//2]
    part2 = numbers[len(numbers)//2:]
    result = [part1, part2]
    print(result)
elif len(numbers) % 2 != 0 or len(numbers) == 1:
    part1 = numbers[0:len(numbers)//2 +1]
    part2 = numbers[len(numbers)//2 +1:]
    result = [part1, part2]
    print(result)
