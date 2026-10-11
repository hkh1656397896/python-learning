m,n=map(int,input().split())
if m<=n:
    s=0
    for i in range (0,n-m+1):
        s=s+(m+i)**2+1/(m+i)
    print(f"sum = {s:.6f}")
