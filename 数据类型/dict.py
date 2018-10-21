obj = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(obj['Michael'])

# 避免key不存在的错误

print('a' in obj)

print(obj.get('a'))

if obj.get('a'):
    print('有')
else:
    print('没有')
