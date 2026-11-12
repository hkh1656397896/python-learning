n=int(input("number:"))
l=[]
cnt=0
for i in range(2,n):
    if n%i==0:
        l.append(i)
        cnt+=1
if cnt!=0:
    print(l)  
else:
    print(f"{n} is prime")
