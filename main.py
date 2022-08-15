count = 1
flag = '1'
while flag != '0':
    f = 0
    k = -1
    print('Введите действие, которое хотите воcпроизвести:\n'
          '0. выйти из адрессной книжки\n'
          '1. показать список контактов\n'
          '2. добавить контакт\n'
          '3. удалить контакт\n'
          '4. изменить контакт\n'
          '5. найти контакт')
    flag = input()

    if flag == '1':
        file = open('adress book.txt', 'r', encoding='UTF-8')
        print(file.read())
        file.close()

    if flag == '2':
        file = open('adress book.txt', 'r+', encoding='UTF-8')
        s = input('Введите Имя и номер контакта: ')
        for line in file.readlines():
            if s == line:
                print('Такой контакт уже сущесвует')
                f = 1
                break
        if f == 0:
            file.write('\n')
            file.write(s)
            print('Контакт успешно добавлен!')
        file.close()

    if flag == '3':
        file = open('adress book.txt', 'r', encoding='UTF-8')
        s = input('Введите Имя и номер контакта: ')
        for line in file.readlines():
            k += 1
            if s == line.rstrip():
                file.seek(0)
                lines = file.readlines()
                del lines[k]
                file.close()
                file = open('adress book.txt', 'w', encoding='UTF-8')
                count = 0
                for line1 in lines:
                    count += 1
                    file.write(line1.rstrip())
                    if count != len(lines):
                        file.write('\n')
                file.close()
                f = 1
                print('Контакт успешно удален!')
                break
        if f == 0:
            print('Такого контакта не существует!')

    if flag == '4':
        file = open('adress book.txt', 'r', encoding='UTF-8')
        s1 = input('Введите имя и номер контакта: ')
        for line in file.readlines():
            k += 1
            if s1 == line.rstrip():
                s2 = input('Введите измененные имя и номер контакта: ')
                file.seek(0)
                lines = file.readlines()
                del lines[k]
                file.close()
                file = open('adress book.txt', 'w', encoding='UTF-8')
                file.writelines(lines)
                file.write('\n')
                file.write(s2)
                f = 1
                print('Контакт успешно изменен!')
                break
        if f == 0:
            print('Такого контакта не существует!')

    if flag == '5':
        file = open('adress book.txt', 'r', encoding='UTF-8')
        s = input('Введите имя контакта для поиска: ')
        for line in file.readlines():
            if s in line:
                print(line.rstrip())
                f = 1
        if f == 0:
            print('Такого контакта не существует!')
        file.close()


    print()

print('Программа завершена...')