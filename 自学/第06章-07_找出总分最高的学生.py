N=int(input())
L=[]
m=[input().split() for _ in range(N)]
for i in range(N):
    t=sum(map(int,m[i][2:5]))
    L.append(t)
for i in range(N):
    if max(L)==sum(map(int,m[i][2:5])):
        print(m[i][1],m[i][0],max(L))