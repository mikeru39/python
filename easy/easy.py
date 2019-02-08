import os


def create_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')


def delete_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
    except FileNotFoundError:
        print('Этого файла не существуетв в текущей директорий')


def change_dir(path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))


def list_dir():
    dir_path = os.path.join(os.getcwd())
    [print(dir) for dir in os.listdir(dir_path)]
