n=int(input())
m=list(input().split(","))
cnt=0
l=[]
for i in range(len(m)):
    if list(m[i]*n)==m[i:i+n]:
        cnt+=1
        s=",".join(m[i]*n)
        l.append((s))
print(cnt)
for ch in l:
    print(ch)

