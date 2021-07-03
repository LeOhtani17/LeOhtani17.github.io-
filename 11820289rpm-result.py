a=input("一つ目の数字を入力してください:")
b=input("二つ目の数字を入力してください:")
c=0
d=0

a=int(a)
b=int(b)

def rpm():
    global a
    global b
    global c
    global d
    while b!=0:
        if b%2!=0:
            c=c+a
            a=a*2
            b=b//2
            if b!=0:
                d=d+2
        
        if b%2==0:
            a=a*2
            b=b//2
            if b!=0:
                d=d+2
        
    print("答えは"+str(c))
    print(str(d)+"回の乗除算が行われている")
        
rpm()    
