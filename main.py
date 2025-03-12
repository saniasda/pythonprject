#Домашнее задание 5.2
while True:
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
    replay = input("Хотите продолжить? (Если да, пропишите 'yes' без ковычек): ").lower()
    if replay != "yes":
        break


