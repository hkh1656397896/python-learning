def sumThree(n):
    cnt=0
    for i in range(1,n+1,2):
        number=[int(c) for c in str(i)]
        k=number.count(3)
        cnt+=k
    return cnt

n=int(input())
print(f"number:{sumThree(n)}")
