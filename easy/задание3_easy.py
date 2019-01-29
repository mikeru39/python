numbers = [2, 5, 3, 0, 1, 20, 10, 8, ]
answer = []
for number in numbers:
    if number % 2 == 0:
        answer.append(number / 4)
    else:
        answer.append(number * 2)
print(answer)
