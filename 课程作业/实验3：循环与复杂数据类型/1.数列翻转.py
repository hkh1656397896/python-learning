m=list(map(int,input().split()))
n=m[0]
l=m[1:n+1]
l.reverse()
s=""
for c in l:
    s+=str(c)+" "
print(s)

