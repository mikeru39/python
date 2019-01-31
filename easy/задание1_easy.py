def user(name, age, city):
    sentence = '{}, {} год(а), проживает в городе {}.'.format(name, age, city)
    return sentence


name = input('Как вас зовут? ')
age = input('Сколько вам лет? ')
city = input('Где вы живете? ')

print(user(name, age, city))
