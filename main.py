#Домашнее задание 3.1
number = int(input("Введите первое число: "))
number1 = int(input("Введите второе число: "))
operation = input("Введите операцию: \n+\n-\n*\n/\n")
if operation == "+" :
    result = number + number1
    print(f"Результат: {result}")
elif operation == "-":
    result = number - number1
    print(f"Результат: {result}")
elif operation == "*":
    result = number * number1
    print(f"Результат: {result}")
elif operation == "/":
    if number1 != 0:
        result = number / number1
        print(f"Результат {result}")
    else:
        print("Деление на 0 невозможно")

#v2 case
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
operation1 = input("Введите операцию: \n+\n-\n*\n/\n")
match operation1:
    case "+":
        result = num1 + num2
        print(f"Результат: {result}")
    case "-":
        result = num1 - num2
        print(f"Результат: {result}")
    case "*":
        result = num1 * num2
        print(f"Результат {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Результат: {result}")
        else:
            print("Деление на 0 невозможно")

#Домашнее задание 3.2
nums = [12, 3, 4, 10, 8]
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)

#Домашнее задание 3.3
nums1 = [1, 2, 3, 4, 5, 6]
middle_index = len(nums1) // 2

if len(nums1) % 2 != 0:
    middle_index += 1

part1 = nums1[:middle_index]
part2 = nums1[middle_index:]
result = [part1, part2]
print(result)

