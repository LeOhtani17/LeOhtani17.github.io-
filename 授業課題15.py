import random
player={"HP":100,"Atk":50,"Dfn":30,"MP":5}

def input_cmd():
    while True:
        cmd=input('攻撃（A)：防御（D):回復 (H)ー＞')
        if cmd=='a' or cmd=='A':
            return 0
        elif cmd=='d' or cmd=='D':
            return 1
        elif cmd=='h' or cmd=='H':
            return 2
        else:
            pass
def battle():
    global cmd
    global dead
    dead=0
    enemy1 = {"Name":"モンスターA",'HP':25,'Atk':20,'Dfn':20}
    enemy2 = {"Name":"モンスターB",'HP':45,'Atk':30,'Dfn':25}
    enemy3 = {"Name":"モンスターC",'HP':30,'Atk':45,'Dfn':15}
    enemy4 = {"Name":"モンスターD",'HP':30,'Atk':20,'Dfn':35}
    enemy_list = [enemy1,enemy2,enemy3,enemy4]
    rnd = random.randint(0,len(enemy_list)-1)
    enemy = enemy_list[rnd]
    print(enemy["Name"],"が現れた！")
    while True:
        print("現在のHP:{}".format(player["HP"]))
        print("Playerの攻撃")
        cmd=input_cmd()
        if cmd==0:
            damage=int((player["Atk"]-enemy["Dfn"]*0.5)*random.randint(25,70)/100)
            print("{}は{}のダメージを与えた".format("Player",damage))
            enemy["HP"]-=damage
            if enemy["HP"]<=0:
                print(enemy["Name"],"をやっつけた！！！")
                break
        if cmd==1:
            print("Playerは防御の体制を取った")
            print(enemy["Name"],"の攻撃")
            damage=int(((enemy["Atk"]-player["Dfn"]*0.5)*random.randint(25,70)/100)*random.randint(30,60)/100)
            print("{}のダメージを受けた".format(damage))
            player["HP"]-=damage
        if cmd==2 and player["MP"]>0:
            print("PlayerはMPを消費した")
            player["MP"]=player["MP"]-1
            recovery=int(random.randint(40,60))
            player["HP"]+=recovery
            print("PlayerのHPが"+str(recovery)+"回復した")
            print(enemy["Name"],"の攻撃")
            damage=int((enemy["Atk"]-player["Dfn"]*0.5)*random.randint(25,70)/100)
            print("{}のダメージを受けた".format(damage))
            player["HP"]-=damage
        else:
            print(enemy["Name"],"の攻撃")
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
    
