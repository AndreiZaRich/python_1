def count_equal_pairs(numbers):
    num_count = {}
    count = 0

    for num in numbers:
        if num in num_count:
            num_count[num] += 1
            if num_count[num] % 2 == 0:
                count += 1
        else:
            num_count[num] = 1

    return count

import random

quantity_elements_list = int(input("Введите количество элементов в массиве: "))
numbers = [random.randint(1, 10) for _ in range(quantity_elements_list)]
print("Сгенерированный массив:", numbers)

# Вызов функции для подсчета пар
pair_count = count_equal_pairs(numbers)
print("Количество пар элементов, равных друг другу:", pair_count)
