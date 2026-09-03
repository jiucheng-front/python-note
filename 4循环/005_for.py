"""
for 乘法表
"""

for row in range(1, 10):
    for cell in range(1, row + 1):
        print(f"{cell} * {row} = {cell * row}\t", end="")
    # 尾部换行一下
    print()