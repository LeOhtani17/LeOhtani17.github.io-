a=" "
b="×"
c="〇"
for i in range(1,9):
    if i%2==0:
        a=b+a
        print(a)
    else:
        a=c+a
        print(a)
