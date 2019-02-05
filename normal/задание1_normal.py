import re

name = input('Введите свое имя: ')
surname = input('Введите свою Фамилия: ')
email = input('Введите свой Email: ')

regex_name = '^[A-ZЁ-Я][a-zа-ё]+$'
regex_email = '^[a-z_0-9]+@[a-z0-9]+\.(com|ru|org)'

error_code = 0

if not re.match(regex_name, name):
    error_code = 1
    print('Неверно указано имя.')
if not re.match(regex_name, surname):
    error_code = 1
    print('Неверно указана фамилия.')
if not re.match(regex_email, email):
    error_code = 1
    print('Неверно указан email.')
if not error_code:
    print('Данные введены верно.')
