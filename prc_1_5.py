s = "45678998765"
print(s)

# print(s.count("4"))
#
# print(set(s))

counts = {c:s.count(c) for c in set(s)}
print(counts)
#
# print(counts.get("5"))
# print(counts["5"])

biggest_3 = sorted(counts, key=counts.get, reverse=True)[:3]
print(biggest_3)