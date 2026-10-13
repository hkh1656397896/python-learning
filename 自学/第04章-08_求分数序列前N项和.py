N=int(input())
a,b=1,2
total=0.00
for _ in range(N):
    total+=b/a
    a,b=b,a+b
print(f"{total:.2f}")