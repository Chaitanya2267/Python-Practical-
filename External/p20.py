s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s1.add(50)
s1.update([50, 60])
s1.remove(10)
s1.discard(20)
s1.pop()
s1.union(s2)
s1.intersection(s2)
s1.difference(s2)
# print({30, 40}.issubset(s2))
s3 = s1.copy()

print(s3)