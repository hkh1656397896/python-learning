N=int(input())
if N==0:
    print("average = 0.0")
    print("count = 0")
else:
    m=list(map(int,input().split()))
    average=sum(m)/len(m)
    count=0
    for i in m:
        if i>=60:
            count+=1
print(f"average = {average:.1f}")
print(f"count = {count}")