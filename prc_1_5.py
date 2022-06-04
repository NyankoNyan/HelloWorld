

s = "45687658658769486378998765"
print(s)

# print(s.count("4"))
#
# print(set(s))

counts = {c: s.count(c) for c in set(s)}
print(counts)
#
# print(counts.get("5"))
# print(counts["5"])

# f = counts.get
#
# print(f("5"))



biggest_3 = sorted(counts, key=counts.get, reverse=True)[:3]
# biggest_3 = sorted(counts, key=counts.get, reverse=True)

# def my_sort(x):
#     return -counts[x]
# biggest_3 = sorted(counts, key=my_sort)
#
# biggest_3 = sorted(counts, key=lambda x:-counts[x])

print(biggest_3)