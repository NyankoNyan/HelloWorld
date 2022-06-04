#numbers = list(range(5))

#with open("serial.txt","w") as file:
#    file.write(str(numbers))

with open("serial.txt", "r") as file:
    content = file.read()

numbers_2 = list(eval(content))
#numbers_2 = [0, 1, 2, 3, 4]
numbers_2.reverse()

for n in numbers_2:
    print(n)
