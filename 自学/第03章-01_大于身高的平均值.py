nums=list(map(int,input().split()))
avg=sum(nums)/len(nums)
for n in nums:
    if n>avg:
        print(n,end=" ")