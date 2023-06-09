import random

count_elehments_fist_list = int(input("Введите количество элементов в первом массиве: "))
fist_list = [random.randint(1, 10) for _ in range(count_elehments_fist_list)]
print("Сгенерированный первый массив:", fist_list)

count_elehments_second_list = int(input("Введите количество элементов во втором массиве: "))
second_list = [random.randint(1, 10) for _ in range(count_elehments_second_list)]
print("Сгенерированный второй массив:", second_list)


result = [x for x in fist_list if x not in second_list]
print(result)
