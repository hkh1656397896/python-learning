a,b=map(int,input().split(","))
cnt=0
for i in range(a,b+1):
    if (i%4==0 and i%100!=0) or i%400==0:
        cnt+=1
        print(i,end=" ")
    if cnt%5==0:
        print()
if cnt==0:
    print("not found")
