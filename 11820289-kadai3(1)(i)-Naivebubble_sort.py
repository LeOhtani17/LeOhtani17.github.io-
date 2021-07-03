import random
b=0
def bubble_sort(sorting):
    global b
    global c
    n=len(sorting)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if sorting[j]>sorting[j+1]:
                a=sorting[j+1]
                sorting[j+1]=sorting[j]
                sorting[j]=a
                b=b+1
            else:
                b=b+1

if __name__=='__main__':
    n=input("配列の数を入力:")
    n=int(n)
    sorting=[random.randint(1,100) for i in range(n)]
    print("元の配列"+str(sorting))
    import time 
    start=time.perf_counter()
    bubble_sort(sorting)
    end=time.perf_counter()
    print("ソート後の配列"+str(sorting))
    print(str(b)+"回比較した")
    print('処理時間={0:.10f}秒'.format(end-start))
