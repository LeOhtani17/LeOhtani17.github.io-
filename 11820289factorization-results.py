n=input("自然数を入力してください:")
n=int(n)
a=3
b=n**0.5

print(str(n)+"の素因数は")

import time
start=time.time()
while a<b:
    if n%2==0:
        n=n/2
        print(2,end=" ")
    elif n%a==0:
        n=n/a
        print(a,end=" ")
    else:
        a=a+2


end=time.time()
print('処理時間={}秒'.format(end-start))
