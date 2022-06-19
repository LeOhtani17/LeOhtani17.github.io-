def bubble_sort():
    global b
    global c
    b=0
    c=0
    n=len(sorting)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if sorting[j]>sorting[j+1]:
                a=sorting[j+1]
                sorting[j+1]=sorting[j]
                sorting[j]=a
                b=b+1
            else:
                c=c+1
                
bubble_sort()
print(str(b)+"回交換し"+str(b+c)+"回比較した")
