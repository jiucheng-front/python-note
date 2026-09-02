
num = 0
while num < 10:
    num += 1
    if num == 5:
        print(f'当前的循环数字是:{num}，后面不循环了')
        break
    print(num)

sum = 0
num2 = 1
while num2 <= 100:
    sum += num2
    num2 += 1
print(sum, num2)