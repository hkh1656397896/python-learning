m=int(input())
a,b=1,1
for _ in range(m):
    a,b=b,a+b
    if a+b>m:
        print(a+b)
        break