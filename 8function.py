
# 递归
def fn(n):
    if n == 1:
        return 1
    return n * fn(n - 1)

print('fn:', fn(5))

# 尾递归优化
def fact(num, pro):
    print('inner_pro:', pro)
    if num == 1:
        return pro
    return fact(num - 1, num * pro)

print('fact:', fact(5, 1))