M,N=list(map(int,input().split()))
for i in range(min(M,N),0,-1):
    if M%i==0 and N%i==0:
        r=i
        break
l=M*N//r
print(f"{r} {l}")



