m=int(input())
s=[input() for _ in range(m)]
r=max(map(len,s))
L=[]
for i,ch in enumerate(s):
    if len(ch)==r:
        L.append(i)
a=min(L)
print(f"The longest is: {s[a]}")
    