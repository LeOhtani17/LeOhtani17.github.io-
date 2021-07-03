a=input("学籍番号(8桁)を入力:")
a=int(a)
b=input("誕生年(和暦)を入力:")
b=int(b)
sum=0
for i in range(1,9):
    sum=sum+int(a[i])
count=0
for d in range(1,int(a)+1):
    if d%b==0 and d%c==0:
        count=count+1
    
print("1から"+str(a)+"までに"+str(b)+"と"+str(c)+"の両方で割り切れる数は"+str(count)+"個")
