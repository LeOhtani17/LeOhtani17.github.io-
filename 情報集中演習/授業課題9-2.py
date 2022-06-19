list = [31,28,31,30,31,30,31,31,30,31,30,31]

month = input("何月？")
month = int(month)

for i in range(1,list[month-1]+1):
    if i%7==0:
        print(i,end='\n')
    else:
        print(i,end='\t')
