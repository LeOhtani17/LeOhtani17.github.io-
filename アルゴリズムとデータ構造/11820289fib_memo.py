memorize={}
def f(n):
    global count
    count=count+1
    if n<3:
        return 1
    if n not in memorize:
        memorize[n]=f(n-1)+f(n-2)
        return memorize[n]

if __name__=="__main__":
    count=0
    for n in range(1,41):
        print(f(n))
    print(str(count)+"回関数を呼び出した")        
