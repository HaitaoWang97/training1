import random
times = 3
secret = random.randint(1,10)
print('------------------深度学习------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    if temp.isdigit():
        guess = int(temp)
        times = times - 1 # 用户每输入一次，可用机会就-1
        if guess == secret:
            print("猜中了！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
            if times > 0:
                print("再试一次吧：", end=" ")
            else:
                print("机会用光咯T_T")
    else:
        print('输入有误，请输入一个整数：',end =' ')
print("游戏结束，不玩啦^_^")
