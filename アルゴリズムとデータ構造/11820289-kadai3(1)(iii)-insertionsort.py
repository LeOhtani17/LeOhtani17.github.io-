c=0
import random
def insertionsort(ary):
    n=len(ary)
    global c
    for i in range(1,n):
        j=i-1
        a=ary[i]
        while ary[j]>a and j>=0:
            ary[j+1]=ary[j]
            j=j-1
            c=c+1
        ary[j+1]=a
        c=c+1
if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    ary=[random.randint(0,100) for i in range(n)]
    print("元の配列"+str(ary))
    import time 
    start=time.perf_counter()
    insertionsort(ary)
    end=time.perf_counter()
    print("ソート後の配列"+str(ary))
    print(str(c)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
