import random

numbs_assess = int(input("Введите количество полученных оценок: "))
assess = [random.randint(1, 5) for _ in range(numbs_assess)]
print("Сгенерированный список оценок:", assess)

def change_assess(assess):
    for i in range(len(assess)):
        if assess[i] > 3:
            assess[i] = 1
    return assess

assess_new = change_assess(assess)
print(assess_new)
