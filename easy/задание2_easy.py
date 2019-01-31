def max_numbers(number_1, number_2, number_3):
    max_number = max(number_1, number_2, number_3)
    return max_number


userAnswer = input('Введите три произвольных числа, через пробел: ')
number_1, number_2, number_3 = userAnswer.split()

print(max_numbers(number_1, number_2, number_3))
