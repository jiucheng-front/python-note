
# list
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
a1 = L[0:3]
print('list:', a1)

A = list(range(100))
# print(A)


# tuple
T = (1, 2,3,4,5)
T1 = (1, 2,3,4,5)[0:3]
print('tuple:', T1)

# Str
S = 'ABCDEFG'
e = len(S) - 1
S1 = S[:3]
print('str:',S1)

S2 = S[-1:]
print('str:', S2)
print('str_end', S[e])

# 练习:去除字符串首尾的空格
strp = ' Hello, World!  '
def remove_space(str):
    str1 = str[:]
    end = len(str1) - 1
    if str1[0] != ' ' and str1[end] != ' ':
        return str1
    elif str1[0] == ' ':
        str1 = str1[1:end]
        return remove_space(str1)
    elif str1[end] == ' ':
        str1 = str1[0:end - 1]
        return remove_space(str1)
    else:
        return str1

print('remove_space:', remove_space(strp))


# 遍历迭代:Iteration
# list遍历
arr = ['a', 'b', 'c']
for s in arr:
    print('list:', s)

# Str遍历
for s in S:
    print('str:', s)

# dict遍历
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print('key:', key)

for value in d.values():
    print('value:', value)

for k,v in d.items():
    item = {k:v}
    print('item:', item)
    print('k:', k)
    print('v:', v)


# 练习:使用迭代查找一个list中最小和最大值，并返回一个tuple：
nums = [1, 2, 3, 6, 9, -1]
# 简单
nums1 = tuple(nums)
max1 = max(nums1)
min1 = min(nums1)
print('max:', max1)
print('min:', min1)
# 遍历
def findMinAndMax(L):
    min = max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)

print('findMinAndMax:', findMinAndMax(nums))


### 列表生成式
arr1 = list(range(1, 11))
print('arr1:', arr1)

arr2 = [x * x for x in range(1, 11)]
print('arr2:', arr2)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str) == True]
L3 = [s if isinstance(s,str) == True else s s.lower() for s in L1]
print('L2:', L2)
print('L3:', L3)