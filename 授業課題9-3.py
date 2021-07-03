dlist = [31,28,31,30,31,30,31,31,30,31,30,31]

a = input("何月？")
a = int(a)
b = input("その月の一日は何曜日？(0=SUN～6=SAT)")
b = int(b)

wlist = ["SUN\t","MON\t","TUE\t","WED\t","THU\t","FRI\t","SAT\t"]
for c in wlist:
    print(c,end="")
print("")

for j in range(b):
    print(end="\t")
    
for i in range(1,dlist[a-1]+1):
    if i%7==7-b:
        print(i,end='\n')
    else:
        print(i,end='\t')
