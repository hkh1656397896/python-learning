n=int(input())
m=int(input())
s=n
for _ in range(m-1):
    n*=0.25
    s+=2*n
    h=n*0.25
print(f"{s:.2f}")
print(f"{h:.2f}")

