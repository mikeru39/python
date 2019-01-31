def max_string(string):
    max_len = max(string, key=len )
    return max_len


string = []
while True:
    userAnswer =(input('Введите любой длины строчку, а для завершения нажмите q: '))
    if userAnswer == 'q':
        break
    else:
        string.append(userAnswer)
print(max_string(string))

