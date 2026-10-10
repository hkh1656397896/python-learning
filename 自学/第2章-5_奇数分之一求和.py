N=int(input())
sum=0
for i in range(1,N+1):
    sum=sum+1/(2*i-1)
print(f"sum = {sum:.6f}")