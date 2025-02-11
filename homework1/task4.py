# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

# Ввод количества секунд
total_seconds = int(input("Введите количество секунд: "))

# Вычисляем количество дней, часов, минут и секунд
days = total_seconds // (24 * 3600)
total_seconds %= (24 * 3600)
hours = total_seconds // 3600
total_seconds %= 360012
minutes = total_seconds // 60
seconds = total_seconds % 60

# Выводим результат в формате дни:часы:минуты:секунды
print(f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд")