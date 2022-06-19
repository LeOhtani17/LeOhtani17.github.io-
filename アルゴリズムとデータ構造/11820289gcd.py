a=input("自然数を入力してください:")
b=input("自然数を入力してください:")

a=int(a)
b=int(b)
c=3
d=3
e=a**0.5
f=b**0.5

listA=[]
listB=[]

while c<e:
    if a%2==0:
        a=a/2
        listA.append(2)
    elif a%c==0:
        a=a/c
        listA.append(c)
    else:
        c=c+2

while d<f:
    if b%2==0:
        b=b/2
        listB.append(2)
    elif b%d==0:
        b=b/d
        listB.append(d)
    else:
        d=d+2

import numpy as np
intersection=[i for i in listA if i in listB]

print("最大公約数は"+str(int(np.prod(intersection))))

