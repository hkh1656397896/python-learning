a,n=input().split()
n=int(n)
s=int(a*n)
for i in range(n-1,0,-1):
    s-=int(a*i)
print(s)
