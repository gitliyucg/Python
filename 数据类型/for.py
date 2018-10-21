names = ['Michael', 'Bob', 'Tracy']

for item in names:
    print(item)
# range()生成一个整数序列
print(list(range(5)))

num = 0
for item in range(101):
    num = num + item
print(num)

# while循环
sum = 0
n = 99
list = []
while n > 0:
    sum = sum + n
    list.append(sum)
    n = n - 2
print(list)
