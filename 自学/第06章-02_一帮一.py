N=int(input())
L=[input().split() for _ in range(N)]
l=[]
for i in range(N//2):
    for j in range(N-1,N//2-1,-1):
        if L[i][0]!=L[j][0] and j not in l:
            print(L[i][1],L[j][1])
            l.append(j)
            break







