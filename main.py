# Домашнее задание 5.3
import string
hashteg = ['Python Community', 'i like python community!', 'Should, I. subscribe? Yes!']
max_len = 140
for current_string in hashteg:
    if len(current_string) > max_len:
        print(current_string + " length more than " + str(max_len) + " characters")
        continue
    current_string = current_string.title()
    current_string = current_string.replace(" ", "")
    for symbol in string.punctuation:
        current_string = current_string.replace(symbol, "")
    current_string = "#" + current_string
    print(current_string)

# Домашнее задание 5.1 =============================================
import keyword
import string

name = input("Введите имя переменной: ")
if name in keyword.kwlist:
    print(False)
elif name[0].isdigit():
    print(False)
elif any(char.isupper() for char in name) or any(char in string.punctuation for char in name):
    print(False)
elif name.count('_') > 1:
    print(False)
else:
    print(True)

#Домашнее задание 6.1
import string
ALL_LETTERS = string.ascii_letters
SEPARATOR = "-"
user_input = input("Введите буквы в формате (а-с): ").strip()
if len(user_input) == 3:
    first_letter = user_input[0]
    second_letter = user_input[2]
    separator = user_input[1]
    if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR:
        start_index = ALL_LETTERS.index(first_letter)
        end_index = ALL_LETTERS.index(second_letter)
        if start_index > end_index:
            start_index, end_index = end_index, start_index
        result = ALL_LETTERS[start_index:end_index + 1]
        print(result)


# #Домашнее задание 6.2
seconds = int(input("Введите количество секунд: "))
if 0 <= seconds < 8640000:
    days, remaining_seconds = divmod(seconds, 86400)
    hours, remaining_seconds = divmod(remaining_seconds, 3600)
    minutes, seconds = divmod(remaining_seconds, 60)
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дни"
    else:
        day_word = "дней"
    print(f"{days} {day_word}, {hours:02}:{minutes:02}:{seconds:02}")
else:
    print("Число должно быть от 0 до 8639999 секунд")

# #Домашнее задание 6.3
number = int(input("Введите число: "))
while number > 9:
    temp_number = str(number)
    result = 1
    for char in temp_number:
        if char.isdigit():
            result *= int(char)
    number = result
print(number)