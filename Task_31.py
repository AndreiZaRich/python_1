def fibo(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input("Введите порядковый номер числа в последовательности Фибоначчи, которое нужно найти: "))
if n == 0:
    result = 0
elif n == 1:
    result = 1
elif n == 2:
    result = 1
else:
    result = fibo(n)

if result is not None:
    print(f"Число Фибоначчи под номером с порядковым номером {n}: {result}")
else:
    print("Ошибка! Введите положительное число для порядкового номера числа в последовательности Фибоначчи.")
