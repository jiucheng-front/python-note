# from abstest import my_abs1;

num = abs(-20)
print(num)

max1 = max(3 ,4, 6, -1)
print(max1)

inta = int('234')
print(inta)


# 定义函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-199))

# print(my_abs1(-498))

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

# 函数的参数
def power(x):
    return x * x
print('power_2_2:', power(2))

def power1(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print('power1_2_3:', power1(2,3))

# 默认参数
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

# 二是如何设置默认参数。
def power3(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print('power3_5_2:', power3(5))


# 可变参数

def calc(nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum

print('calc_1:', calc([1,2,3]))
print('calc_2:', calc((1,2,3,4)))

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print('calc1_1:', calc1(1,2,3))

nums = [1, 2, 3]
print('calc1_2:', calc1(*nums))

# 关键字参数
def person(name, age, **kw):
    print('person:','name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
# 简化写法
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Jack', 24, **extra)

# 练习
def multiply(*args):
    """支持直接传入多个数，或传入一个列表/元组"""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        # 如果只有一个参数且是列表或元组，则使用它
        numbers = args[0]
    else:
        numbers = args
    
    if not numbers:
        return 0
    
    result = 1
    for num in numbers:
        result *= num
    return result

# 使用示例
print('multiply1:', multiply(2, 3, 4))        # 输出: 24
print('multiply2:', multiply([2, 3, 4]))      # 输出: 24
print('multiply3:', multiply((2, 3, 4)))      # 输出: 24
print('multiply4:', multiply(5))              # 输出: 5