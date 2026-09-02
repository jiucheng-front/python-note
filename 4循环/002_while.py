

import random
num = random.randint(1, 100)

isGuessRight = True
count = 0
while isGuessRight:
    guessNum = int(input("请输入猜测的数字"))
    count += 1
    if guessNum == num:
        isGuessRight = False
        print("恭喜你猜中了")
    else:
        if guessNum > num:
            print("猜大了")
        else:
            print("猜小了")

print(f"一共猜测{count}次")