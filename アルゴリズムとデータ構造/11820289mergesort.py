def mergesort(ary):
    n=len(ary)
    if n==1:
        return ary
    mid=n//2
    l=(ary[:mid])
    r=(ary[mid:])
    if len(l)==0 or len(r)==0:
        return l or r
    merge(l,r)

def merge(l,r):
    c={}
    i=0
    j=0
    n=len(l)
    m=len(r)
    while i<=n-1 and j<=m-1:
        if l[i]<=r[j]:
            c.append(l[i])
            i=i+1
        else:
            c.append(r[j])
            j=j+1
    if i<=n-1 and i>m-1:
        c.append(l[i:])
    elif i>n-1 and i<=m-1:
        c.append(r[j:])
    return c
    

    
