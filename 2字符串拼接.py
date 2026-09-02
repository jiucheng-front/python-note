
"""
格式化拼接符号
%s  字符串占位符
%d  整数占位符
%f  浮点数占位符

数字进度控制，会四舍五入
%m.n
%.nf 小数点后几位
"""
def my_func():
    # user_name = input("Enter your name: ")
    user_name = "娃哈哈"
    user_age = 18
    user_height = 1.65
    print("大家好，我是%s, 今年是%d岁，身高是%f" % (user_name, user_age, user_height))
    print("大家好，我是%s, 今年是%3d岁，身高是%.3f" % (user_name, user_age, user_height))

my_func()


"""
快速拼接字符串
fxx{变量} 原样输出
"""

def my_fun1():
    user_name = "娃哈哈"
    user_age = 18
    user_height = 1.65
    print(f"我是:{user_name},现在是:{user_age}岁,身高是:{user_height}")
    print(f"格式化表达式1：{2 * 2}, 格式化表达式2: {type('字符串')}")

my_fun1()