#домашнее задание 2.1
number = int(input("Введите 4-значное число: "))
num1 = number // 1000
num2 = number // 100 % 10
num3 = number // 10 % 10
num4 = number % 10
print(num1,num2,num3,num4, sep="\n")

#домашнее задание 2.2

number1 = int(input("Введите 5-значное число: "))

n1 = number1 % 10
n2 = number1 // 10 % 10
n3 = number1 // 100 % 10
n4 = number1 // 1000 % 10
n5 = number1 // 10000

result = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5
print(result)