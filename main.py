#Домашнее задание 4.1

numbers = [3, 0, 4, 5, 0, 7, 8, 0, 15, 12, 0]
min_value = min(numbers)
max_value = max(numbers)
min_value_index = numbers.index(min_value)
max_value_index = numbers.index(max_value)
numbers[min_value_index], numbers[max_value_index] = numbers[max_value_index], numbers[min_value_index]
num1 = [num for num in numbers if num != 0]
num2 = [0] * numbers.count(0)
numbers = num1 + num2
print(numbers)

#Домашнее задание 4.2

numbers = [0, 1, 7, 2, 4, 8]
print(numbers)
num1 = numbers[::2]
num2 = sum(num1)
result = num2 * numbers[-1] \
    if numbers else 0
print(result)

#Домашнее задание 4.3

import random

NUMS_SIZE = 10
numbers = []
for i in range(NUMS_SIZE):
    numbers.append(random.randint(1, 10))
result = [numbers[0], numbers[2], numbers[-2]]
print(numbers)
print(result)


