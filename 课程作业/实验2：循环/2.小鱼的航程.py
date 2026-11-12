s=input()
li=s.split()
x=int(li[0])
n=int(li[1])
cnt=x
km=0
for i in range(n):
    if 1<=cnt<=5:
        km+=250
    cnt+=1
    if cnt>7:
        cnt=1
print(km)

