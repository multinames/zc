#Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

# Задаем список
numbers = [1, 2, 3, 4, 5, 237, 6, 8, 10, 12]

# Проходим по элементам списка
for number in numbers:
    if number == 237:
        print("Встретили 237, останавливаемся.")
        break  # Останавливаем выполнение, если встречаем 237
    if number % 2 == 0:  # Проверяем, является ли число четным
        print(number)