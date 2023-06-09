import random

quantity_elehments_list = int(input("Введите количество элементов в массиве: "))
list = [random.randint(1, 10) for _ in range(quantity_elehments_list)]
print("Сгенерированный массив:", list)

count_pair = 0
for element in range(len(list)):
    if element > 0 and element < len(list) - 1:
        if list[element - 1] < list[element] > list[element + 1]:
            count_pair = count_pair +1

print("Количество элементов, у которых два соседних и,")
print("при этом, оба соседних элемента меньше данного: ", count_pair)