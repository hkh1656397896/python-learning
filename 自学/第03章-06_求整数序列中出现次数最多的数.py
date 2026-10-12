n=input().split()
m=int(n[0])
N=n[1:m+1]
store=[]
for x in N:
    if x not in store:
        store.append(x)
r=max(N.count(x) for x in store)
l=[x for x in store if N.count(x)==r]
L=int(l[0])
print(L,r)



