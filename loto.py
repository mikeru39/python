import random

Player_kard = [
    {"1s": " ", "2s": "  ", "3s": "  ", "4s": "  ", "5s": "  ", "6s": "  ", "7s": "  ", "8s": "  ", "9s": "  "},
    {"1s": " ", "2s": "  ", "3s": "  ", "4s": "  ", "5s": "  ", "6s": "  ", "7s": "  ", "8s": "  ", "9s": "  "},
    {"1s": " ", "2s": "  ", "3s": "  ", "4s": "  ", "5s": "  ", "6s": "  ", "7s": "  ", "8s": "  ", "9s": "  "}
]
Computer_kard = [
    {"1s": " ", "2s": "  ", "3s": "  ", "4s": "  ", "5s": "  ", "6s": "  ", "7s": "  ", "8s": "  ", "9s": "  "},
    {"1s": " ", "2s": "  ", "3s": "  ", "4s": "  ", "5s": "  ", "6s": "  ", "7s": "  ", "8s": "  ", "9s": "  "},
    {"1s": " ", "2s": "  ", "3s": "  ", "4s": "  ", "5s": "  ", "6s": "  ", "7s": "  ", "8s": "  ", "9s": "  "}
]
keys = ['1s', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s']
use_numbers = []
barrels = []
Closed_cells_of_player = 0
Closed_cells_of_computer = 0
top_limit = 90

for i in range(1, 91):
    barrels.append(i)


def Random_number():
    number = random.randint(1, 90)
    n = 0
    while n < 3:
        for i in use_numbers:
            if i == number:
                number = random.randint(1, 90)
        n += 1
    return number


def Random_numbers(list, index_of_list):
    i = 0
    while i < 5:  # Заполнение строчки.
        number = Random_number()
        n = 0
        low_limit = 0
        top_limit = 9

        while n < 10:
            if top_limit == 89:
                top_limit += 1
            if low_limit <= number <= top_limit:
                item = list[index_of_list].get(keys[n])
                if item == '  ' or item == ' ':
                    list[index_of_list][keys[n]] = number
                    use_numbers.append(number)
                    i += 1
                    break
                else:
                    break

            low_limit += 10
            top_limit += 10
            n += 1


def Kard_full(kard):
    i = 0
    while i < 3:
        Random_numbers(kard, i)
        i += 1


def print_kard(kard, player):
    if player == 'computer':
        print('-- Карточка компьютера ---')
    else:
        print('------ Ваша карточка -----')

    print(' {} {} {} {} {} {} {} {} {}'.format(kard[0]['1s'], kard[0]['2s'], kard[0]['3s'],
                                               kard[0]['4s'], kard[0]['5s'], kard[0]['6s'],
                                               kard[0]['7s'], kard[0]['8s'], kard[0]['9s']))
    print(' {} {} {} {} {} {} {} {} {}'.format(kard[1]['1s'], kard[1]['2s'], kard[1]['3s'],
                                               kard[1]['4s'], kard[1]['5s'], kard[1]['6s'],
                                               kard[1]['7s'], kard[1]['8s'], kard[1]['9s']))
    print(' {} {} {} {} {} {} {} {} {}'.format(kard[2]['1s'], kard[2]['2s'], kard[2]['3s'],
                                               kard[2]['4s'], kard[2]['5s'], kard[2]['6s'],
                                               kard[2]['7s'], kard[2]['8s'], kard[2]['9s']))
    print('--------------------------\n')


def check_answer(player, number):
    answer = 0
    i = 0
    while i < 3:
        for key, item in player[i].items():
            if item == number:
                if item <= 9:
                    player[i][key] = "-"
                    answer = 1
                    i += 3
                    break
                else:
                    player[i][key] = "--"
                    answer = 1
                    i += 3
                    break
            else:
                answer = 0
        i += 1
    return answer


Kard_full(Player_kard)
Kard_full(Computer_kard)

print('========== Лото ==========')
while True:
    top_limit -= 1
    number = random.randint(0, top_limit)
    number = barrels.pop(number)

    print('Новый бочонок: {} (осталось {})'.format(number, top_limit))
    print_kard(Player_kard, 'player')
    print_kard(Computer_kard, 'computer')
    userAnswer = input('Зачеркнуть цифру? (y/n): ')
    if userAnswer == 'y':
        if check_answer(Player_kard, number) == 1:
            Closed_cells_of_player += 1
        else:
            print('Вы проиграли.')
            break
    else:
        if check_answer(Player_kard, number) == 1:
            print('Вы проиграли.')
            break

    if Closed_cells_of_player == 15:
        print('Вы выйграли!!')
        break

    if check_answer(Computer_kard, number) == 1:
        Closed_cells_of_computer += 1

    if Closed_cells_of_player == 15:
        print('Вы проиграли.')
        break
