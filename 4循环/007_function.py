
"""
函数
介绍、定义、参数、返回值、说明、嵌套调用、作用域、案例
"""

# 提前写好，可重复使用

# 函数的参数：形式参数，动态变化的
def my_add(a, b):
    return a + b
def my_sub(a, b):
    return a - b
def my_mult(a, b):
    return a * b
def my_div(a, b):
    return a / b

# 调用函数时：参数是实际参数
num1 = my_add(1, 2)
print(num1)
num2 = my_mult(num1, 3)
print(num2)

# 函数也可以作为形式参数传递：前提内部有return
num4 = my_div(my_mult(num1, 3), my_add(1, 2))
print(num4)