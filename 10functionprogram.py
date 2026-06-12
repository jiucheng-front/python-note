# 高阶函数
def add1(x, y, f):
    return f(x) + f(y)

print('heigh-function:', add1(10, -20, abs))

def f(x):
    return x * x


# map
r = map(f, [1,2,3,4,5])
print('map:', list(r))

# 把数字转为字符串
sn = list(map(str, [1,2,3,4,5,6,7,8]))
print('map_2:', sn)

# reduce
from functools import reduce
def add2(x, y):
    return x + y

sum = reduce(add2, [1,3,5,7,9])
print('reduce1:', sum)

# 练习首字母大写
def ftr(str):
    return str[0].upper() + str[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(ftr, L1))
print('map_3:', L2)