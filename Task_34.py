def check_rhythm(poem):
    syllables = []
    for phrase in poem.split():
        phrase_syllables = []
        for word in phrase.split('-'):
            num_syllables = count_syllables(word)
            phrase_syllables.append(num_syllables)
        syllables.append(phrase_syllables)
    return all(phrase == syllables[0] for phrase in syllables)

def count_syllables(word):
    vowels = 'аеёиоуыэюя'
    count = sum(1 for letter in word.lower() if letter in vowels)
    return count

# Ввод стихотворения
poem = input("Введите стихотворение Винни-Пуха: ")

# Проверка количества слов в стихотворении
if len(poem.split()) == 1:
    print("Это одно слово, нужно ввести стихотворение")
else:
    # Проверка ритма
    if check_rhythm(poem):
        print("Парам пам-пам")
    else:
        print("Пам парам")
