import random
x=random.randint(1,1001)
count=0
while True:
    y=range(1,1001)
    y=input("1から1000の数値を入力 = ")
    y=int(y)
    if x<y:
        print(str(y)+"より小さい")
        count=count+1
    elif x>y:
        print(str(y)+"より大きい")
        count=count+1
    else:
        count=count+1
        print(str(count)+"回で正解！！")
        break
