
#Напишите программу, которая объединяет два словаря и суммирует значения одинаковых ключей.

#Словарь 1
dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 200,
         'апельсины': 300, 'ананасы': 45, 'лимоны': 98,
         'сливы': 76, 'манго': 34, 'виноград': 90, 'лаймы': 230}
#Словарь 2
dict2 = {'яблоки': 300, 'груши': 200, 'бананы': 400,
         'малина': 777, 'ананасы': 12, 'лаймы': 123, 'черника': 111, 'арбузы': 666}


#todo Решение



# dict1['яблоки'] - яблоки - ключ
# a = dict1['яблоки'] в a будет значение

#'яблоки': 100
#'яблоки': 300
# dict3['яблоки'] = 100 + 300

dict3 = {}

for key1 in dict1:
    dict3[key1] = dict1[key1]

for key2 in dict2:
    if key2 in dict3:
        dict3[key2] = dict3[key2] + dict2[key2]
    else:
        dict3[key2] = dict2[key2]

all_keys = set(dict1) | set(dict2)
dict3={}
for key in all_keys:
    dict3[key] = dict1.get(key, 0) + dict2.get(key, 0)

#dict3 = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
for key in sorted(dict3):
    print(f"{key}:{dict3[key]}")
    print(key + ":" + str(dict3[key]))
    print("%s:%d" % (key,dict3[key]))
print(dict3)


#print("Объединенный словарь:", merged_dict)





