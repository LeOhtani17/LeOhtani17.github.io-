def battle():
    print(str(cnt+1)+"回戦")
    print("バトルをします")
    global cmd
    cmd=""
    cmd=input("何かキーを押してください")
    print("バトルが終わりました")
cnt=0
while cnt<3:
    battle()
    cnt=cnt+1
    if cmd=="e" or cmd=="E":
        break
