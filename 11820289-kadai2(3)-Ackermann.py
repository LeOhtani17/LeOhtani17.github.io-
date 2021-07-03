memo=[]
c=0
def ack(m,n):
    global c
    c=c+1
    if m==0:
        return n+1
    if (m,n) not in memo:
        if m!=0 and n==0:
            memo[(m,n)]=ack(m-1,1)
        else:
            memo[(m,n)]=ack(m-1,ack(m,n-1))
    return memo[(m,n)]

if __name__=="__main__":
    m=input("非負整数を入力:")
    n=input("非負整数を入力:")
    m=int(m)
    n=int(n)
    import time
    start=time.perf_counter()
    ack(m,n)
    end=time.perf_counter()
    print(c)
    print('処理時間={0:.10f}秒'.format(end-start))
