print("Возьмите любое количество монет. Подбросьте каждую вверх и дайте ей упасть на любую поверхность.")
print("Каждая монета упала орлом или решкой вверх. Примем 1 за орла и 0 за решку.")
print("Если вдруг монета осталась стоять на ребре (ну вы и везунчик ;),")
print("переподбросте ее столько раз сколько потребуется, чтобы она упала орлом или решкой.")
print("В следующей строке последовательно введите какой стороной упала кажная монета. Например, вы бросили 5 монет, тогда введите: 10011")
coins = input("Введите последовательность: ")
num_coins = len(coins)                                  # узнаем длину строки
flag = 0                                                # флаг для окончания цикла
coins0 = 0                                              # количество монет упавших решкой
coins1 = 0                                              # количество монет упавших орлом
char = 1                                                # счетчик символов в строке
while flag < num_coins:                                 # проверяем не закончились ли символы в строке
    flag += 1
    if coins.isdigit():                                 # проверяем все ли символы в строке можно перевести в цифры
        side = int(coins[-char])                        # переводим символы в числа, начиная с последнего
        char += 1
        if side == 0:                                   # далее, в строках 17-20, проверяем орел или решка и суммируем их
            coins0 += 1
        elif side == 1:
            coins1 += 1
        else:       # здесь сообщаем о неправильном вводе (есть другие цифры, кроме 1 и 0) и просим ввести заново
            print("Вы, вообще, бросали монеты? Или так кнопки понажимать пришли? :) Будьте внимательны.")
            coins = input("Введите последовательность снова: ")
            num_coins = len(coins)
            flag = 0
            coins0 = 0
            coins1 = 0
            char = 1
    else:       # здесь сообщаем о неправильном вводе (есть другие символы, кроме цифр) и просим ввести заново
        print("Вы, вообще, бросали монеты? Или так кнопки понажимать пришли? :) Будьте внимательны.")
        coins = input("Введите последовательность снова: ")
        num_coins = len(coins)
        flag = 0
        coins0 = 0
        coins1 = 0
        char = 1
# Вот не хватило у меня батареек написать код по другому в двух предыдущих else, кроме как код сдублировать :(
else:
    if coins0 > coins1 and coins0 != num_coins and coins0 != 0:
        print("Чтобы все монеты лежали одной стороной, вам нужно перевернуть, всего лишь, вот столько монет ", coins1)
    elif coins0 < coins1 and coins0 != num_coins and coins0 != 0:
        print("Чтобы все монеты лежали одной стороной, вам нужно перевернуть, всего лишь, вот столько монет ", coins0)
    else:
        print("Вам повезло! Ни одну монету не нужно переворачивать. Заберите их все :)")

# Код, конечно, кривоватенький и мне не очень нравится...
# Но зато сам написал :)
# Код написанный ChatGPT, приведенный ниже, значительно красивее.
# Но я писал операторами и функциями, которые знаю и понимаю на данный момент.
# П.С. Вторую лекцию еще не посмотрел. Как всегда со временем беда...

# import random
#
# n = int(input("Введите количество монеток: "))
# coins = []
#
# for _ in range(n):
#     coin = random.choice([0, 1])  # генерируем случайное положение монетки
#     coins.append(coin)
#
# heads = sum(coins)  # количество монеток, лежащих гербом
# tails = len(coins) - heads  # количество монеток, лежащих решкой
#
# min_flips = min(heads, tails)
#
# print("Количество монеток:", n)
# print("Положение монеток:", coins)
# print("Минимальное количество монет, которые нужно перевернуть:", min_flips)