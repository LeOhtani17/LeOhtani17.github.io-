import random
a=input("誕生年を入力(和暦):")
a=int(a)
count=0
b=list(range(1,26))
random.shuffle(b)
for i in b:
    count=count+1
    if count%5==0:
        print(i,end="\n")
    else:
        print(i,end="\t")
    if a==i:
        c=count
if c%5==0:
    print(str(a)+"は"+str(c//5)+"行"+str(5)+"列にあります")
else:
    print(str(a)+"は"+str(c//5+1)+"行"+str(c%5)+"列にあります")
