def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a - 1, b + 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

result = sum(a, b)
print("Сумма чисел a и b:", result)
