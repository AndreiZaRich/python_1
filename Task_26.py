def a_power_b(a, b):
    a_next = a
    for i in range(b - 1):
        a_next = a_next * a
    return a_next

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
power = a_power_b(a, b)
print("a в степени b будет равно:", power)
