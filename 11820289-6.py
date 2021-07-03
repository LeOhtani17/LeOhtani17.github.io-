import random
me={"Money":10000}
dealer={"money":10000}
count=0
while True:
    c1=random.randint(1,14)
    c2=random.randint(1,14)
    count=count+1
    print("ターン"+str(count)+" 現在の資産は{}".format(me["Money"])+"円")
    print("あなたのカードは"+str(c1))
    print("ディーラーのカードは"+str(c2))
    if c1>c2 and c2!=1:
        print("あなたの勝ち")
        me["Money"]=me["Money"]+1000
        dealer["money"]=dealer["money"]-1000
    elif c1<c2 and c1!=1:
        print("ディーラーの勝ち")
        me["Money"]=me["Money"]-1000
        dealer["money"]=dealer["money"]+1000
    elif c1==1 and c1!=c2:
        print("あなたの勝ち")
        me["Money"]=me["Money"]+1000
        dealer["money"]=dealer["money"]-1000
    elif c2==1 and c1!=c2:
        print("ディーラーの勝ち")
        me["Money"]=me["Money"]-1000
        dealer["money"]=dealer["money"]+1000
    elif c1==c2:
        print("ドロー")
        pass
    if me["Money"]<=0:
        print("ディーラーの勝ち")
        print("あなたは破産しました")
        break
    elif dealer["money"]<=0:
        print("あなたの勝ち")
        print("ディーラーを破産させました")
        break
