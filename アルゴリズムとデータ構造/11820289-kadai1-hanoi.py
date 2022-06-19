def hanoi(n,A,B,C):
    if n==1:
        print("{}:{}→{}".format(n,A,B))
    else:
        hanoi(n-1,A,C,B)
        print("{}:{}→{}".format(n,A,B))
        hanoi(n-1,C,B,A)

print(hanoi(5,"A","B","C"))
