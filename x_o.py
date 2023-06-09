field = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def fieldPrint(field):
    print(field[0], " ", field[1], " ", field[2])
    print(field[3], " ", field[4], " ", field[5])
    print(field[6], " ", field[7], " ", field[8])


def checkWinCombination(field):
    if (field[0] == field[1] == field[2]) or (field[3] == field[4] == field[5]) or (
            field[6] == field[7] == field[8]) or (field[0] == field[3] == field[6]) or (
            field[1] == field[4] == field[7]) or (field[2] == field[5] == field[8]) or (
            field[0] == field[4] == field[8]) or (field[2] == field[4] == field[6]):
        return True
    else:
        return False


fieldPrint(field)
count = 0
win = False
while (win == False):

    if (count >= 5):
        win = checkWinCombination(field)

    print("YOUR ARE NEXT:")
    target = int(input())
    field[target] = "X"
    count += 1
    print(count)
    fieldPrint(field)
    print()

    if (count >= 5):
        win = checkWinCombination(field)

    print("COMP GO")
    for i in range(0, 8):
        if (field[i] != "X") and (field[i] != "O"):
            field[i] = "O"
            break
    count += 1

    print(count)
    fieldPrint(field)
    print()