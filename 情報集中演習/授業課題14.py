import random
player={"HP":100,"Atk":50,"Dfn":30}

def battle():
    global cmd
    global dead
    dead=0
    enemy={"HP":100,"Atk":50,"Dfn":30}
    while True:
        print("現在のHP:{}".format(player["HP"]))
        print("Playerの攻撃")
        cmd=input("攻撃（A)：防御（D)->")
        if cmd=="a" or cmd=="A":
            damage=int((player["Atk"]-enemy["Dfn"]*0.5)*random.randint(25,70)/100)
            print("{}は{}のダメージを与えた".format("Player",damage))
            enemy["HP"]-=damage
            if enemy["HP"]<=0:
                print("Enemyをやっつけた！！！")
                break
        if cmd=="d" or cmd=="D":
            print("Playerは防御の体制を取った")
            print("Enemyの攻撃")
            damage=int(((enemy["Atk"]-player["Dfn"]*0.5)*random.randint(25,70)/100)*random.randint(30,60)/100)
            print("{}のダメージを受けた".format(damage))
            player["HP"]-=damage
        else:
            print("Enemyの攻撃")
            damage=int((enemy["Atk"]-player["Dfn"]*0.5)*random.randint(25,70)/100)
            print("{}のダメージを受けた".format(damage))
            player["HP"]-=damage
        if player["HP"]<=0:
            dead=1
            print("Playerは死にました....")
            break
        print("............")

if __name__=="__main__":
    cnt=0
    while cnt<3:
        print(str(cnt+1)+"回戦")
        battle()
        cnt=cnt+1
        if cmd=="e" or cmd=="E" or dead==1:
            break
    
