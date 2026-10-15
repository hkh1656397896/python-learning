m=input().split()
i=0
for _ in range(3): 
    L=[m[i],m[i+3],m[i+6]]
    i+=1
    x="".join(f"{c:>4}" for c in L)
    print(x)
