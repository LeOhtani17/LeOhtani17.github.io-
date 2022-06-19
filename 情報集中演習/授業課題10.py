dlist=[31,28,31,30,31,30,31,31,30,31,30,31]
youbi=["日","月","火","水","木","金","土"]

a=input("何年?:")
a=int(a)
b=input("一月一日の曜日を入力(0=日曜日～6=土曜日)")
b=int(b)

if a%4==0  or a%400==0:
    dlist[1]=29
elif a%100==0:
    dlist[1]=28
for l in range(1,13):
    for k in youbi:
        print(k,end="\t")
    print("")

    count=0
    for j in range(b):
        print(" ",end="\t")
        count=count+1

    for i in range(1,dlist[l-1]+1):
        count=count+1
        if count%7==0:
            print(i,end="\n")
        else:
            print(i,end="\t")
    b=count%7
    print("")
