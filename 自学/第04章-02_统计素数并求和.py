M,N=map(int,input().split())
yes=0
L=[]
for n in range(M,N+1):
    if n<=1:continue
    for i in range(2,n):   
        if n%i==0:break
    else:
        yes+=1
        L.append(n)
print(f"{yes} {sum(L)}")
