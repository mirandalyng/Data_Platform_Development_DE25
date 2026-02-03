# Pair programming task

numbers = [3, 1, 4, 2, 5, 2]

tmp = []

for number in numbers:
    if tmp.__contains__(number):
        print(number)
    else:
        tmp.append(number)

duplicate_array = [i for i in set(numbers) if numbers.count(i) > 1]
print(duplicate_array)
