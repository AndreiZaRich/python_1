import random

numbs_assess = int(input("Введите количество полученных оценок: "))
assess = [random.randint(1, 5) for _ in range(numbs_assess)]
print("Сгенерированный список оценок:", assess)

def change_assess(assess):
    for i in range(len(assess)):
        max_assess = max(assess)
        min_assess = min(assess)
        if assess[i] == max_assess:
            assess[i] = min_assess
    return assess

assess_new = change_assess(assess)
print(assess_new)
