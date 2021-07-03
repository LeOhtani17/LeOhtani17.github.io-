def f(n):
    global count
    count+=1
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

        
if __name__=='__main__':
    count=0
    for n in range(1,41):
        print(f(n))
    print(str(count)+'回f(n)をコールした')