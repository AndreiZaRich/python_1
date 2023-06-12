a = int(input("Введите первый элемент (a): "))
d = int(input("Введите разность (d): "))
n = int(input("Введите количество элементов (n): "))

progression = [a + i * d for i in range(n)]
print("Массив элементов арифметической прогрессии:")
print(progression)
