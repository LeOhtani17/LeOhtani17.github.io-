def f(n,k):
    global count
    count=count+1
    if n<0 or k<0 or n<k:
        return 0
    elif n==0 or k==0:
        return 1
    return f(n-1,k-1)+f(n-1,k)

if __name__=="__main__":
    count=0
    for k in range(0,11):
        print(f(n,k),end="")
        print()
        print(str(count)+"回関数がコールされた")
