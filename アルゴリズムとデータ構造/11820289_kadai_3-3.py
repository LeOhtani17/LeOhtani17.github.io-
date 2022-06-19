def selectionsort(ary):
    n=len(ary)
    global d
    global e
    d=0
    e=0
    for i in range(0,n-1):
        a=i
        for j in range(i+1,n):
            if ary[a]>ary[j]:
                a=j
                e=e+1
    b=ary[a]
    ary[a]=ary[i]
    ary[i]=b
    d=d+1

n=input("配列の数を入力:")
selectionsort(ary)
print(str(d)+"回比較し"+str(e)+"回交換した")
