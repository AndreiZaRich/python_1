def reverse(n):
    if n == 0:
        return
    num = int(input("Введите число: "))
    reverse(n - 1)
    print(num)

# Вводим количество элементов последовательности
n = int(input("Введите количество элементов последовательности: "))

# Вызываем функцию для вывода последовательности в обратном порядке
reverse(n)
