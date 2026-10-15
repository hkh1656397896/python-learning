import string
n=int(input())
i=0
a,b=0,n
L=string.ascii_uppercase
for _ in range(n):
    print(*L[a:b],sep=" ",end=" \n")
    a,b=b,b+n-1
    n-=1
    i+=1
while i==n:break
