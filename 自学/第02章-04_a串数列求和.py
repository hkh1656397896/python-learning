a,n=map(int,input().split())
if 1<=a<=9 and 1<=n<=9:
    s=0
    for i in range(1,n+1):
       s=s+int(str(a)*i)
print(f"s = {s}")
