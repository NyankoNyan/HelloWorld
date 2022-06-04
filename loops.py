# алгоритмы на циклы (поиск элемента, ё

# Перебор
# a = [1, 2, "test"]
#
# for elem in a:
#     print(elem)
#     print(str(elem) + " хрень")

# Вложенные циклы
# for x in range(3):
#     for y in range(5):
#         for z in range(2):
#             print(f"[{x}, {y}, {z}] ", end="")
#         print()
#     print()

# Вложенные списки
# people = [
#     ["Денис",    31, "программист"],
#     ["Виталька", 30, "программист"],
#     ["Венеамин", 16, "программист"],
#     ["Женя",     31, "леньтяй"]
# ]
#
# for e in people:
#     print("Это " + e[0] + ", ему " + str(e[1]) + " и он " + e[2])
#
# yongest = people[0]
# for e in people:
#     if e[1] < yongest[1]:
#         yongest = e
#
# # yongest = min(people, key=lambda e: e[1])
#
# print("А самый младший у нас " + yongest[0])


class Person:
    def __init__(self, name, age, prof):
        self.name = name
        self.age = age
        self.prof = prof

people = [
    Person("Денис",    31, "программист"),
    Person("Виталька", 30, "программист"),
    Person("Венеамин", 16, "программист"),
    Person("Женя",     31, "леньтяй")
]

for e in people:
    print("Это " + e.name + ", ему " + str(e.age) + " и он " + e.prof)

if len(people)>0:
    yongest = people[0]
    for e in people:
        if e.age < yongest.age:
            yongest = e

    print("А самый младший у нас " + yongest.name)

# Поиск элемента
# Простой
# people = [
#     "Денис",
#     "Виталька",
#     "Венеамин",
#     "Женя"
# ]
#
# print(people.index("Венеамин"))

# Сложный
# people = [
#     ["Денис", 31, "программист"],
#     ["Виталька", 30, "программист"],
#     ["Венеамин", 16, "программист"],
#     ["Женя", 31, "леньтяй"]
# ]
#
# # person=[]
# # for e in people:
# #     if e[2] == "программист":
# #         person = e
# #         break
# #
# # print(person)
#
# print(list(filter(lambda e:e[2]=="программист", people)))