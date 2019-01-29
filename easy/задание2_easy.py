first_list = [2, 2, 4, 2, 6, 1, 1, 9, 10, 20]
second_list = [2, 5, 3, 0, 1, 20, 10, 8, ]
while True:
    result = list(set(first_list) & set(second_list))
    if result != []:
        i = 0
        while i < len(result):
            first_list.pop(first_list.index(result[i]))
            i += 1
    else:
        break

print(first_list, second_list)
