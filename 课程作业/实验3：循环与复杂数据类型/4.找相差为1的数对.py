n=int(input())
m=list(map(int,input().split()))
p=set()
l=[]
for i in m:
    if i-1 in m:
        p.add((i-1,i))
for ch in p:
    l.append(ch)
l.sort()
if len(l)==0:
    print(0)
else:
    print(len(l))
    for j in l:
        for k in j:
            print(k,end=" ")
        print()

