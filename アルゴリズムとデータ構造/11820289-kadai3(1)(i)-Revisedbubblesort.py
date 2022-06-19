import random
c=0
def bubblesort(a):
    global c
    n=len(a)
    for i in range(n,1,-1):
        flag=True
        for j in range(1,i):
            c=c+1
            if a[j-1]>a[j]:
                flag=False
                a[j-1],a[j]=a[j],a[j-1]
        if flag==True:
            break
    return a

if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    a=[random.randint(0,100) for i in range(n)]
    print("元の配列"+str(a))
    import time 
    start=time.perf_counter()
    bubblesort(a) 
    end=time.perf_counter()
    print("ソート後の配列"+str(a))
    print(str(c)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
