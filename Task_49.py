import os

source = 'phonebook.txt'

# Функция для чтения данных из файла
def readData(fileName):
    try:
        with open(fileName) as f:
            phoneBook = []
            for line in f:
                phoneBook.append([item.rstrip('\n') for item in line.split(',')])
        return phoneBook
    except FileNotFoundError:
        print("File not found.")
        return []

# Функция для записи данных в файл
def writeData(fileName, phoneBook):
    try:
        with open(fileName, 'w') as f:
            for entry in phoneBook:
                f.write(','.join(entry) + '\n')
            print("Data successfully saved.")
    except:
        print("Error occurred while saving data.")

# Функция для вывода всех записей
def selectAllReadPhoneNumber():
    phoneBook = readData(source)
    for entry in phoneBook:
        print(entry)

# Функция для поиска записи по номеру телефона
def selectSomethingReadPhoneNumber():
    phoneBook = readData(source)
    phoneNumber = str(input("Enter telephone number: "))
    found = False
    for entry in phoneBook:
        if phoneNumber == entry[4]:
            print("ID              :", entry[0])
            print("SURNAME         :", entry[1])
            print("FIRST_NAME      :", entry[2])
            print("SECOND_NAME     :", entry[3])
            print("TELEPHONE_NUMBER:", entry[4])
            print("")
            found = True
    if not found:
        print("No records found.")

# Функция для добавления новой записи
def addPerson():
    phoneBook = readData(source)
    maxID = 0
    for entry in phoneBook:
        if maxID < int(entry[0]):
            maxID = int(entry[0])
    print("Enter data")
    number = str(maxID + 1)
    surname = str(input("Enter surname: "))
    nameFirst = str(input("Enter first name: "))
    nameSecond = str(input("Enter second name: "))
    phoneNumber = str(input("Enter telephone number: "))
    entry = [number, surname, nameFirst, nameSecond, phoneNumber]
    phoneBook.append(entry)
    writeData(source, phoneBook)
    print(phoneBook)

# Функция для редактирования записи
def editPerson():
    phoneBook = readData(source)
    print("Edit data:")
    selectSomethingReadPhoneNumber()
    print("Do you want to change the details of a person?")
    if answerUserYesOrNo() == 'Y':
        print("Enter ID to edit person:")
        editID = int(answerUserNumberIndex(phoneBook))
        for entry in phoneBook:
            if editID == int(entry[0]):
                print("ATTENTION! EDIT PERSON MOD: ON")
                print("ID              :", entry[0])
                print("SURNAME         :", entry[1])
                print("FIRST_NAME      :", entry[2])
                print("SECOND_NAME     :", entry[3])
                print("TELEPHONE_NUMBER:", entry[4])

                print("Edit SURNAME ?")
                newSurName = answerUserYesOrNo()
                if newSurName == 'Y':
                    newSurName = str(input("Enter surname: "))
                else:
                    newSurName = entry[1]

                print("Edit FIRST_NAME ?")
                newFirstName = answerUserYesOrNo()
                if newFirstName == 'Y':
                    newFirstName = str(input("Enter first name: "))
                else:
                    newFirstName = entry[2]

                print("Edit SECOND_NAME ?")
                newSecondName = answerUserYesOrNo()
                if newSecondName == 'Y':
                    newSecondName = str(input("Enter second name: "))
                else:
                    newSecondName = entry[3]

                print("Edit TELEPHONE_NUMBER ?")
                newPhoneNumber = answerUserYesOrNo()
                if newPhoneNumber == 'Y':
                    newPhoneNumber = str(input("Enter telephone number: "))
                else:
                    newPhoneNumber = entry[4]

                print("ID              :", editID)
                print("SURNAME         :", entry[1], "==>", newSurName)
                print("FIRST_NAME      :", entry[2], "==>", newFirstName)
                print("SECOND_NAME     :", entry[3], "==>", newSecondName)
                print("TELEPHONE_NUMBER:", entry[4], "==>", newPhoneNumber)
                print("Are you sure about these changes?")
                if answerUserYesOrNo() == 'Y':
                    entry[1] = newSurName
                    entry[2] = newFirstName
                    entry[3] = newSecondName
                    entry[4] = newPhoneNumber
                    writeData(source, phoneBook)
                    print("Edit saved.")
                else:
                    print("Edit not saved.")
    else:
        print("Edit canceled.")

# Функция для удаления записи
def deletePerson():
    phoneBook = readData(source)
    print("Delete data:")
    selectSomethingReadPhoneNumber()
    print("Do you want to delete the person?")
    if answerUserYesOrNo() == 'Y':
        print("Enter ID to delete person:")
        deleteID = int(answerUserNumberIndex(phoneBook))
        for entry in phoneBook:
            if deleteID == int(entry[0]):
                print("ATTENTION! DELETE PERSON MOD: ON")
                print("ID              :", entry[0])
                print("SURNAME         :", entry[1])
                print("FIRST_NAME      :", entry[2])
                print("SECOND_NAME     :", entry[3])
                print("TELEPHONE_NUMBER:", entry[4])
                print("Are you sure you want to delete this person?")
                if answerUserYesOrNo() == 'Y':
                    phoneBook.remove(entry)
                    writeData(source, phoneBook)
                    print("Delete saved.")
                else:
                    print("Delete canceled.")
    else:
        print("Delete canceled.")

# Функция для проверки ответа пользователя (Y/N)
def answerUserYesOrNo():
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = str(input("Enter Y or N: ")).upper()
    return answer

# Функция для проверки ответа пользователя (цифра от 1 до 9)
def answerUserNumberIndex(phoneBook):
    index = ''
    while not index.isdigit() or int(index) > len(phoneBook):
        index = str(input("Enter index number (1 - {}): ".format(len(phoneBook))))
    return index

# Функция для очистки экрана
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Основной цикл программы
def mainLoop():
    while True:
        print("Phonebook Menu:")
        print("1. Select all phone numbers")
        print("2. Select phone number by surname")
        print("3. Add new person")
        print("4. Edit person")
        print("5. Delete person")
        print("6. Exit")
        choice = str(input("Enter your choice (1-6): "))
        clearScreen()
        if choice == '1':
            selectAllReadPhoneNumber()
        elif choice == '2':
            selectSomethingReadPhoneNumber()
        elif choice == '3':
            addPerson()
        elif choice == '4':
            editPerson()
        elif choice == '5':
            deletePerson()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
        print("")  # Добавляем пустую строку для разделения вывода

# Запуск основного цикла программы
mainLoop()
