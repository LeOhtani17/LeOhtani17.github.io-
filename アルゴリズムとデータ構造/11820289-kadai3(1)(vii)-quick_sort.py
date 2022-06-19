import random
b=0
def quick_sort(a,l,r):
    n=len(a)
    if l<r:
        i=partition(a,l,r)
        quick_sort(a,l,i-1)
        quick_sort(a,i+1,r)
    return a

def partition(a,l,r):
    global b
    pivot=a[r]
    i=l-1
    j=r
    while True:
        while True:
            i=i+1
            b=b+1
            if a[i]>=pivot:
                break
        while True:
            j=j-1
            if a[j]<pivot:
                break
        if i>=j:
            break
        a[i],a[j]=a[j],a[i]
    a[i],a[r]=a[r],a[i]
    return i

if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    a1=[17]
    a2=[random.randint(0,100) for i in range(n)]
    a=a1+a2
    print("元の配列"+str(a2))
    l=1
    r=n
    import time 
    start=time.perf_counter()
    quick_sort(a,l,r)
    end=time.perf_counter()
    del a[0]
    print("ソート後の配列"+str(a))
    print(str(b)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
