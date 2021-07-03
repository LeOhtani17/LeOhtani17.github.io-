def a(n):
    if n==0:
        return 0
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return a(n-1)+a(n-2)+a(n-3)

