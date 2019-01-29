lst = [1, 2, 4, 5, 6, 2, 5, 2]
print(set(lst))

lst2 = []
d = {}
for i in lst :
  d[i] = d.get(i, 0) + 1
for key, value in d.items() :
  if value == 1 :
    lst2.append(key)
print (lst2)
