#Найдите наименьшую обыкновенную дробь, равную вещественному числу 14.375, и выведите ее на экран в формате '14.375 = числитель/знаменатель'

from fractions import Fraction

# Заданное вещественное число
number = 14.375

# Преобразуем вещественное число в дробь
fraction = Fraction(number).limit_denominator()

# Выводим результат
print(f"{number} = {fraction.numerator}/{fraction.denominator}")