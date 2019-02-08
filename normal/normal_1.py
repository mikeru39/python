import easy_hw.easy

userAnswer = ''
while userAnswer != '5':
    userAnswer = int(input('1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n'
                           'Ваш ответ: '))
    if userAnswer == 5:
        break

    elif userAnswer == 1:
        path = input('Укажите папку для перехода: ')
        easy_hw.easy.change_dir(path)

    elif userAnswer == 2:
        easy_hw.easy.list_dir()

    elif userAnswer == 3:
        name = input('Введите название  удаляемой папки: ')
        easy_hw.easy.delete_dir(name)

    else:
        name = input('Введите название новой папки: ')
        easy_hw.easy.create_dir(name)
