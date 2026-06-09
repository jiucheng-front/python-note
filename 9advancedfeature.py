
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

