# План:
# + 0) Что такое with
# + 1) Показать базовый алгоритм
# + 2) Показать как хорошо делать в питоне
# + 3) Показать сериализацию
# Нахуй генераторы !!!

# Получили что ввёл юзер
x = int(input('Сколько чисел записать в файл? '))

# Забили список числами
number_list = []
for i in range(1, x+1):
    number_list.append(i)




# Открываем файл
with open('write.txt', 'w') as file:
#file = open('write.txt', 'w')
# Запись каждого числа через пробел
    out_str = ' '.join(str(number) for number in number_list)
#for x in mylist:
#    out_str += ' ' + str(x)
#    file.write(str(x) + "\n")
    file.write(out_str)

# Закрываем файл
#file.close()

# Выводим инфу юзеру
print('Записали', len(number_list), "number's")