n=int(input())
for j in range(1,n+1):
    for i in range(1,j+1):
        t=i*j
        if i==j:
            print(f"{i}*{j}={t:<4}",end="")
            print()      
        else:print(f"{i}*{j}={t:<4}",end="")
