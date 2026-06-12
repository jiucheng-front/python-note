# 高阶函数
def add (x, y, f):
    return f(x) + f(y)

print('heigh-function:', add(10, -20, abs))