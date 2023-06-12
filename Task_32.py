import random

# Ввод пользователем диапазона и количество элементов
minimum = int(input("Введите минимум: "))
maximum = int(input("Введите максимум: "))
quantity = int(input("Введите количество элементов: "))

# Создание списка случайных чисел
numbers = [random.randint(minimum, maximum) for _ in range(quantity)]
print(numbers)

# Ввод пользователем искомого диапазона
search_min = int(input("Введите минимум искомого диапазона: "))
search_max = int(input("Введите максимум искомого диапазона: "))

# Поиск индексов элементов, удовлетворяющих условию
indices = [index for index, num in enumerate(numbers) if search_min <= num <= search_max]

# Вывод списка индексов
print("Список индексов:", indices)
