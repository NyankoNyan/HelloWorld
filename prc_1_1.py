my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
#my_dict2 = {v:k for k,v in my_dict.items()}

# biggest_keys = sorted(my_dict, key=my_dict.get, reverse=True)[0:3]
dict2 = {k: my_dict[k] for k in sorted(my_dict, key=my_dict.get, reverse=True)[0:3]}
print(dict2)

# result = {}
#
# for _ in range(3):
#     first_elem = True
#     for k, v in my_dict.items():
#         if first_elem or max_el_value < v:
#             max_el_key = k
#             max_el_value = v
#             first_elem = False
#
#     result[max_el_key] = max_el_value
#     del my_dict[max_el_key]
#
# print(result)

