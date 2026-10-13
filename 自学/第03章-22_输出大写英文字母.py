import string
c=string.ascii_uppercase
m=input()
L=[]
yes=0
for i in m:
    if i in c:
        yes+=1
        if i in L:continue
        L.append(i)
if yes==0:
    print("Not Found")
else:
    x="".join(L)
    print(x)