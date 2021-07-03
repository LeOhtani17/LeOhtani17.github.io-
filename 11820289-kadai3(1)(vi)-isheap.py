import random
c=0
def down_heap(a,j,k):
    global c
    v=a[j]
    while 2*j<=k:
        i=2*j
        if i<k and a[i]<a[i+1]:
            i=i+1
        c=c+1
        if v<a[i]:
            a[j]=a[i]
            j=i
            c=c+1
        else:
            c=c+1
            break
    a[j]=v
        
def heap_sort(a):
    n=len(a)-1
    for i in range(n//2,0,-1):
        down_heap(a,i,n)
    for k in range(n,1,-1):
        a[1],a[k]=a[k],a[1]
        down_heap(a,1,k-1)

if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    a1=[17]
    a2=[random.randint(0,100) for i in range(n)]
    print("元の配列"+str(a2))
    a=a1+a2
    import time 
    start=time.perf_counter()
    heap_sort(a)
    end=time.perf_counter()
    del a[0]
    print("ソート後の配列"+str(a))
    print(str(c)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
