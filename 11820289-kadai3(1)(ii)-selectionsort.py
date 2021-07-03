d=0
import random
def selectionsort(ary):
    n=len(ary)
    global d
    for i in range(0,n-1):
        a=i
        for j in range(i+1,n):
            if ary[a]>ary[j]:
                a=j
        ary[a],ary[i]=ary[i],ary[a]
        d=d+1
        
if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    ary=[random.randint(0,100) for i in range(n)]
    print("元の配列"+str(ary))
    import time 
    start=time.perf_counter()
    selectionsort(ary)
    end=time.perf_counter()
    print("ソート後の配列"+str(ary))
    print(str(d)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
