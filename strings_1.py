# Строки
# Строковые функции
# Примеры работы с ними

s = "Крутая строка с буковами"

# Длина (не в байтах, а в символах)
l = len(s)
#print(l)

# Перебор букв
# for i in range(len(s)): #range(0, 24)
#     print(s[i])

# Перебор букв в.2
#for c in s:
#    print(c)

# Обрезка строк (подстроки)
# s1 = s[0:5] # Первые 5 букв
# s2 = s[-5:] # От 5ой с конца до конца строки
# s3 = s[7:13] #"строка"
#
# print(s1)
# print(s2)
# print(s3)

# Разделение строки по символам
# sub_words_1 = s.split()
# sub_words_2 = s.split("с")
#
# print(sub_words_1)
# print(sub_words_2)
#
# test_url = "https://www.google.com/search?q=python+string+fynctions&newwindow=1&sxsrf=ALiCzsZUvyVgL3HeuehWayErzkFDne6gzA%3A1654188369241&ei=UemYYvuiDsKQrgT517TYAg&ved=0ahUKEwi7j4_xm4_4AhVCiIsKHfkrDSsQ4dUDCA0&uact=5&oq=python+string+fynctions&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBAgAEA0yBggAEB4QDTIGCAAQHhANMgYIABAeEA06BwgjELADECc6BwgAEEcQsAM6BAgjECc6CwgAEIAEELEDEIMBOggIABCABBCxAzoFCAAQgAQ6BQgAEMsBOgUIIRCgAToGCAAQHhAWSgQIQRgASgQIRhgAUPMCWK0hYLwiaAJwAXgAgAF4iAGvC5IBBDE0LjOYAQCgAQHIAQrAAQE&sclient=gws-wiz"
# site, params = test_url.split("?")
#
# print(site)
#
# param_list = params.split("&")
# for param in param_list:
    # param_name, param_value = param.split("=")
    # print(f'Параметр "{param_name}" имеет значение "{param_value}"')

# Склейка списка строк
# param_list = [  "q=python+string+fynctions",
#                 "newwindow=1",
#                 "sxsrf=ALiCzsZUvyVgL3HeuehWayErzkFDne6gzA%3A1654188369241"]
#
# params = '&'.join(param_list)
# print(params)

# Размер буков
# print(s.lower())
# print(s.upper())
# print(s.capitalize())

# Обрезка символов
# s = " returns the last position "
# print(s.lstrip().lstrip("r"))
# print(s.rstrip())
# print(s.strip())

# Центр
# print("-"*50)
# print(s.center(50))
# print("-"*50)

# Поиск подстроки
# s = "Крутая строка с буковами"
#s = "Крутая строка с буковами"
# if s.count(" ") > 0:
#     print("Error")

s = "Крутая строка с буковами"
# print(s.replace("о","0"))
#
# place = s.index("строка")
# print(place)
# print(s[place:])
#
# print(s[s.index("строка"):])
# print(s.replace("о","0").replace("т","t").replace("у","Y"))
#
# spec_o = ''.maketrans("оту", "0tY")
#
# print(s.translate(spec_o))
# s = "ору с тупости"
# print(s.translate(spec_o))

# s = "(  )"
# s1 = s.replace(")", "(").replace("(", ")")
# print(s1)
#
# spec_o = ''.maketrans("()", ")(")
# print(s.translate(spec_o))