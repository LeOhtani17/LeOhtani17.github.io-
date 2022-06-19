a=input("1つ目の自然数を入力:")
b=input("2つ目の自然数を入力:")
a=int(a)
b=int(b)

import time

start=time.time()
while a%b!=0:
    c=a%b
    a=b
    b=c
end=time.time()

print("最大公約数は"+str(b))
print("処理時間={}秒".format(end-start))
