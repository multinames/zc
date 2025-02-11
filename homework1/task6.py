#Создайте простой калькулятор, который позволяет пользователю вводить два числа и выполнять над ними основные арифметические операции (сложение, вычитание, умножение, деление).

def calculator():
    print("Простой калькулятор")
    
    # Ввод первого числа
    num1 = float(input("Введите первое число: "))
    
    # Ввод второго числа
    num2 = float(input("Введите второе число: "))
    
    # Выбор операции
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    operation = input("Введите номер операции (1/2/3/4): ")

    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Ошибка: Деление на ноль!")
    else:
        print("Ошибка: Неверный выбор операции.")

# Запуск калькулятора
calculator()