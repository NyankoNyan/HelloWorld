from functools import reduce
print(reduce( lambda s, i: s+i if i % 3 == 0 or i % 5 == 0 else s, range(1000), 0))