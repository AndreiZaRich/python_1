def prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Примеры использования функции
num = int(input("Введите число: "))
if prime(num):
    print("yes")
else:
    print("no")
