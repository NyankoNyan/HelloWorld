def to_dict(in_l):
    result = {}
    for e in in_l:
        result[e] = e
    return result


def to_dict2(in_l):
    return {e: e for e in in_l}


my_list = ["a", "b"]
print(my_list)

print(to_dict(my_list))
print(to_dict2(my_list))

def spisok_to_slovar(x):
    return {number: number for number in x}

spisok = [1, 3, 17, 31]
spisok2 = ['a','v','p']

print(  spisok_to_slovar(spisok2)  )