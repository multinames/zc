#Создайте программу, которая генерирует случайное число в определенном диапазоне и выводит его на экран.

import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Задайте диапазон
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

# Генерируем случайное число
random_number = generate_random_number(min_value, max_value)

# Выводим число на экран
print(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")