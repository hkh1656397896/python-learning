T=int(input())
for _ in range(T):
    s=[]
    n=int(input())
    L=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j>=i:continue
            else:s.append(L[i][j])
    if any(s)==0:
        print("YES")
    else:print("NO")



                                 