file = open('write.txt', 'r')

file_content = file.read()
file.close()

number_list = [int(s) for s in file_content.split(' ')]
#for line in file_content.split(' '):
#    reversed_list.append(int(line))

reversed_list = list(reversed(number_list))

print('Прочитали:', number_list)
#reversed_list.reverse()
print('Перевернули:', reversed_list)

file = open('write.txt', 'w')

out_str = ' '.join(str(number) for number in reversed_list)
file.write(out_str)
#for x in reversed_list:
#    file.write(str(x)+" ")
file.close()

#a b c
#c b a
#5 10 20
#'02 01 5'
#'20' '10' '5'
# Hello world!
# !dlrow olleH
# world! Hello