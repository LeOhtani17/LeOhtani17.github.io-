import random
count=0
b=list(range(1,26))
random.shuffle(b)
a=list(b)
for i in b:
    count=count+1
    if count%5==0:
        print(i,end="\n")
    else:
        print(i,end="\t")
