def merge(a,b):
    c={}
    i=0
    j=0
    while i<=n-1 and i<=m-1:
        if a<=b:
            c.append(a)
            i=i+1
        else:
            c.append(b)
            j=j+1
    if i<=n-1 and i>m-1:
        c.append(a)
    elif i>n-1 and i<=m-1:
        c.append(b)

        return c
    
