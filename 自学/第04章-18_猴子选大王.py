m=int(input())
L=list(range(1,m+1))
i=0
while len(L)>1:
    i=(i+2)%len(L)
    L.pop(i)
print(L[0])

