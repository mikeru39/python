import shutil
import os

name_file = os.path.realpath(__file__)
new_file = name_file + '.copy'

if os.path.isfile(new_file) != True:
    shutil.copy(name_file, new_file)
    print(new_file + ' - создан')
else:
    print('Файл уже скопирован')
