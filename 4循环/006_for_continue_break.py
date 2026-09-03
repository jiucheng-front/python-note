"""
发工资余额 1000，员工20名，绩效随机数，小于5的不发，余额发完了剩下的不发
"""
import random
amount = 10000

for p in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工：{p},绩效分为{num}小于5分，不发工资")
        continue
    if amount >= 1000:
        amount -= 1000
        print(f"向员工:{p}发放1000元,绩效分为：{num},账户余额为：{amount}")
    else:
        print(f"工资发完了，员工：{p}下个月领取吧")
        break
