m=list(input())
a,b=input().split()
L=[]
for i,ch in enumerate(m):
    if a==ch or b==ch:
        L.append(i)
for i in sorted(L,reverse=True):
    print(i,m[i])        

