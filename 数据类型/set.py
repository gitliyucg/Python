s = set([1, 2, 3])
print(s)

s.add(4)

print(s)

s.remove(4)

print(s)

# 交集并集处理

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])

s3 = s1 & s2
print(s3)
s3 = s1 | s2
print(s3)
