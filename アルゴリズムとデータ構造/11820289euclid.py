a=input("1つ目の自然数を入力:")
b=input("2つ目の自然数を入力:")
a=int(a)
b=int(b)

while a%b!=0:
    c=a%b
    a=b
    b=c

print("最大公約数は"+str(b))
