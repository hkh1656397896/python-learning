n=int(input())
cnt=0
L=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if L[i][j]>=max(L[i]) and L[i][j]<=min([row[j] for row in L]):
            cnt+=1
print(cnt)
