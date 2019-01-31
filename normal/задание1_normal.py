import os

path = os.path.join('salary.txt')
names, salary = ['саша', 'миша', 'максим', 'дима'], [5000000, 123000, 20000, 6000]
file_list = []
i = 0

for name in names:
    names[i] = name.upper()
    i += 1

dictionary = dict(zip(names, salary))
print(dictionary)

with open(path, 'w+', encoding='UTF-8') as file:
    # запись в файл
    for key, value in dictionary.items():
        file.write('{} - {} \n'.format(key, value))

    # чтение из файла
    file.seek(0)
    for line in file:
        file_list.append(line)

i = 0
for worker in file_list:
    worker = worker.split()
    if int(worker[2]) <= 500000:
        print('{} - {} руб.'.format(worker[0], int(int(worker[2]) * 0.87)))
    else:
        print('{} руб.'.format(int(int(worker[2]) * 0.87)))
