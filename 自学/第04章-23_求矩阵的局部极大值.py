M,N=map(int,input().split())
x=[list(map(int,input().split())) for _ in range(M)]
cnt=0
for i in range(1,M-1):
    for j in range(1,N-1):
        if x[i][j]>x[i-1][j] and x[i][j]>x[i+1][j] and x[i][j]>x[i][j-1] and x[i][j]>x[i][j+1]:
            cnt+=1
            print(x[i][j],i+1,j+1)
if cnt==0:
    print("None",M,N)
        