print("Хотите получить немного счастья? Тогда достаньте свой билет на проезд в общественном транспорте.")
number_ticket = int(input("Введите его номер (число должно быть шестизначное и положительное): "))
if number_ticket > 99999 and number_ticket <1000000:                    # определяем, находится ли число в нужном диапозоне
    first_part = number_ticket % 1000                                   # выделяем число из трёх последних цифр билета
    second_part = (number_ticket - first_part) // 1000                  # выделяем число из трёх первых цифр билета
    ones1 = first_part % 10                                             # выделяем единицы из трёх последних цифр билета
    tens1 = ((first_part - ones1) % 100) // 10                          # выделяем десятки из трёх последних цифр билета
    hundreds1 = ((first_part - ones1 - tens1 * 10) % 1000) // 100       # выделяем сотни из трёх последних цифр билета
    number_summ1 = ones1 + tens1 + hundreds1                            # получаем сумму трёх последних цифр билета
    ones2 = second_part % 10                                            # далее строки 10-13 аналогично для трёх первых цифр билета
    tens2 = ((second_part - ones2) % 100) // 10
    hundreds2 = ((second_part - ones2 - tens2 * 10) % 1000) // 100
    number_summ2 = ones2 + tens2 + hundreds2
    if number_summ1 == number_summ2:                                    # сравниваем полученные суммы
        print("Поздравляю!!! У вас счастливый билет! Съешьте его немедленно, везунчик!! ;)")
    else:
        print("Упс, сегодня звёзды не сошлись... Ну, ничего, в следующий раз обязательно повезёт!!!")
else:
    print("Вы ввели неправильный номер билета.")
    print("Нужно ввести шестизначное положительное число.")
    print("Попробуйте ещё раз.")
    print("P.S. Внимательнее, внимательнее, а то счастье пройдет мимо вас:).")
    # Задание 6 выполнено