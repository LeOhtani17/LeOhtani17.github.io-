def insertionsort(ary):
    n=len(ary)
    global c
    global d
    c=0
    d=0
    for i in range(1,n):
        j=i-1
        a=ary[i]
        while ary[j]>a and j>=0:
            ary[j+1]=ary[j]
            j=j-1
            c=c+1
        ary[j+1]=a
    d=d+1

n=input("配列の数を入力:")
insertionsort(ary)
print(str(c)+"回比較し"+str(d)+"回交換した")
