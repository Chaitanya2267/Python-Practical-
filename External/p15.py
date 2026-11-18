import array

a = array.array('i', [10, 20, 30, 40])

a.append(50)
a.insert(1, 15)
a.remove(30)
a.pop()
# print(a.index(20))
# print(a.count(10))
a.reverse()
a.extend([60, 70])
# print(a.tolist())
print(a.buffer_info())

# print(a)