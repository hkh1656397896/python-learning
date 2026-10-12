m=list(input())
L=[]
yes=0
for i in m:
    if i.isdigit():
        I=int(i)
        yes+=1
        L.append(I)
if yes!=0:
    x="".join(map(str,L))
    print(int(x))
if yes==0:
    print(0)


