# 列表生成式
list1 = [x * x for x in range(1, 11)]
# print(list1)
list2 = [x * x for x in range(1, 11) if x % 2 == 0]
# print(list2)
# 双层循环
list3 = [m + n for m in 'ABC' for n in 'XYZ']
# print(list3)

import os
os1 = [d for d in os.listdir('.')]
print(os1)

L = ['Hello', 'World', 18, 'Apple', None]
L1 = [s.lower() for s in L if isinstance(s, str)]
print(L1)

print(__file__)
