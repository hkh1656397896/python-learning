import string
m=input()
c=string.ascii_letters 
L=[]
s=set()
for i in m:
    if i in c:
        k=i.lower()
        if k in s:
            continue
        s.add(k)      
        L.append(i)
        if len(s)==10:break
if len(s)<10:
    print("not found")
else:
    print("".join(L))
