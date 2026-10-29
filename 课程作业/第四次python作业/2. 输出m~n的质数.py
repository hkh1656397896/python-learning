m,n=map(int,input().split(","))
cnt=0
for i in range(m,n+1):
    for z in range(2,int(i**0.5)+1):
        if i%z==0:
            break
    else:
        cnt+=1
        print(f"{i:<5}",end="")
    if cnt%5==0:
        print()
if cnt==0:
    print(0)

