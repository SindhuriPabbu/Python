a = [3,2,1,4,6,8,7,5]
#length
print(a)
b = len(a)
a.sort()
print(a)
a.extend([10,8,9])
print(a)
print("MAX:",max(a))
print("MIN:",min(a))
print("Count:",a.count(5))
a.append(11)
print(a)
print(a.pop())
a.remove(7)
print(a)
a.reverse()
print("Reverse:",a)
print(a.index(6))
b = a.copy()
print("B:",b)
a.clear()
print(a)
del(a)
#print(a)
