c=0
def Ack(m,n):
    global c
    c=c+1
    if m==0:
        return n+1
    if m!=0 and n==0:
        return Ack(m-1,1)
    else:
        return Ack(m-1,Ack(m,n-1))
    print("int(n+1)")
    
if __name__=='__main__':
    m=input("非負整数を入力:")
    n=input("非負整数を入力:")
    m=int(m)
    n=int(n)
    import time
    start=time.perf_counter()
    Ack(m,n)
    end=time.perf_counter()
    d=Ack(m,n)
    print(str(m)+"と"+str(n)+"の時の関数の値は"+str(d))
    print("関数は"+str(c)+"回呼び出された")
    print('処理時間={0:.10f}秒'.format(end-start))
