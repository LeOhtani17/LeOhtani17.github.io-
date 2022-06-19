d=0
import random
def shakersort(a):
    n=len(a)-1
    global d
    l=2
    r=n
    k=0
    while l<=r:
        for j in range(r,l-1,-1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                k=j
            d=d+1    
        l=k+1
        for j in range(l,r+1):
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                k=j
            d=d+1    
        r=k-1
    return a

if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    a1=[17]
    a2=[random.randint(0,100) for i in range(n)]
    a=a1+a2
    print("元の配列"+str(a2))
    import time 
    start=time.perf_counter()
    shakersort(a)
    end=time.perf_counter()
    del a[0]
    print("ソート後の配列"+str(a))
    print(str(d)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
