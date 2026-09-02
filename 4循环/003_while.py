"""
while 打印乘法表
print不换行
print("11", end="")
print("11", end="")
制表符\t让多行字符串上下对齐

"""

row = 1
while row <=9:
    cell = 1
    while cell <= row:
        print(f"{cell} * {row} = {cell * row}\t", end="")
        cell += 1
    row += 1
    # 这里是行的换行
    print()