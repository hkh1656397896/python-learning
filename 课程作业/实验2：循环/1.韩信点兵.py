n=int(input())
for i in range(1,n+1):
    if i%3==2 and i%5==1 and i%7==0:
        print(i,end=" ")
