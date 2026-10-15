m=int(input())
s=0
a=[list(map(int,input().split())) for _ in range(m)]
for i in range(m-1):
    for j in range(m-1):
        if i+j==m-1:continue
        s+=a[i][j]
print(s)     
