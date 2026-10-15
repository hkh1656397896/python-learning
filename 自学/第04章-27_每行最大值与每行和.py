m=list(map(int,input().split()))
i=0
for _ in range(3):
    L=m[i:i+3]
    i+=3
    x="".join(f"{c:4}" for c in L)
    print(f"{x}{max(L):4}{sum(L):4}")
