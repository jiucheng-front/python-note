"""
for 循环输出乘法表
"""
# 横向行数是1-9行，不包括10
for row in range(1, 10):
    # 当前行的列数从1到当前行*行
    for cell in range(1, row + 1):
        print(f"{cell} * {row} = {cell * row}\t", end="")
    # 尾部换行一下
    print()
