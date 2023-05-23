number = int(input("Введите любое трехзначное положительное число: "))
if  number < 100 or number > 999:
    print("Вы меня разочаровали. Я просил ввести трехзначное положительное число. Фух... Теперь нужно начинать все заново!")
else:
    ones = number % 10
    tens = ((number - ones) % 100) // 10
    hundreds = ((number - ones - tens * 10) % 1000) // 100
    number_summ = ones + tens + hundreds
    print("Сумма цифр введенного трехзначного положительного числа равна ", number_summ)