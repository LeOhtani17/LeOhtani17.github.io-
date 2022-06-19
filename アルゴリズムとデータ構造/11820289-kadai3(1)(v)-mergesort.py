d=0
import random
def mergesort(ary):
    n=len(ary)
    if n==1:
        return ary
    mid=n//2
    l=mergesort(ary[:mid])
    r=mergesort(ary[mid:])
    if not(len(l)) or not(len(r)):
        return l or r
    return merge(l,r)

def merge(a,b):
    global c
    global d
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        d=d+1
        if a[i]<=b[j]:
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    if i<=len(a) and j>=len(b):
        c.extend(a[i:])
    elif i>=len(a) and j<=len(b):
        c.extend(b[j:])
    return c
if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    ary=[random.randint(0,100) for i in range(n)]
    print("元の配列"+str(ary))
    import time 
    start=time.perf_counter()
    mergesort(ary)
    end=time.perf_counter()
    print("ソート後の配列"+str(c))
    print(str(d)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
    
