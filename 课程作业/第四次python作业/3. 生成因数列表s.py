n=int(input())
L=[]
for p in range(1,int(n**0.5)+1):
    q=n//p
    if isinstance(q,int):
        if p!=q:
            L.append(p),L.append(q)
        else:
            L.append(p)
l=sorted(L)
print(l)

