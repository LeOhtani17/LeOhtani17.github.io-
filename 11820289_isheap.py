def down_heap(a,j,k):
    v=a
    while 2j<=k:
        i=2j
        if i<k and a[i]<a[i+1]:
            i=i+1
        if v<a[i]:
            j=i
        else:
            break
    a[j]=v
        
def heap_sort(a):
    n=len(a)
    global b
    for i in range(0,n//2)[::-1]:
        down_heap(a,i,n)
    for k in range(1,n)[::-1]:
        a[1]=b
        a[1]=a[k]
        b=a[k]
        down_heap(a,1,k-1)
