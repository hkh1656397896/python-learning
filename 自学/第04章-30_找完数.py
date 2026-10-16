m,n=map(int,input().split())
l=0
for i in range(m,n+1):
    cnt=1
    k=[1]
    for x in range(2,int(i**0.5)+1):
        if i%x==0:
            cnt+=x
            k.append(x)
            q=i//x
            if q!=x:
                cnt+=q
                k.append(q)
            if  q==x:continue
    if i==cnt:
        l+=1
        y=" + ".join(map(str,sorted(k)))
        print(f"{i} = {y}")
if l==0:
    print("None")
    






