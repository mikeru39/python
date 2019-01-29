import math

numbers = [2, -5, 8, 9, -25, 25, 4]
answer = []
for number in numbers:
    if number >= 0:
        if int(100 * number ** 0.5) % 100 == 0:
            answer.append(int((math.sqrt(number))))

print(answer)
