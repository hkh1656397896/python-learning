total=list(map(int,input().split(',')))
m=int(input())
cnt=0
for a,x in enumerate(total):
    for b,y in enumerate(total):
        if m==x+y and a<b:
            cnt+=1
            print(f"{a} {b}")
            break
if cnt==0:
    print("no answer")

    