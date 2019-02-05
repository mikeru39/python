fruits_1 = ['яблоки', 'мандарин', 'груша', 'банан']
fruits_2 = ['яблоки', 'груша', 'апельсин', 'банан']
rezult = []

[rezult.append(i) for i in (set(fruits_1) & set(fruits_2))]
print(rezult)
