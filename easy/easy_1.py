import os

i = 1
userAnswer = int(input("Вы хотите:\n"
                       "1)Создать новые директории.\n"
                       "2)Удалить директории.\n"
                       ""))
if userAnswer == 1:
    while i <= 9:
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')
        i += 1
else:
    i = 1
    while i <= 9:
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            os.rmdir(dir_path)
        except FileNotFoundError:
            print('Этого файла не существуетв в текущей директорий')
        i += 1
