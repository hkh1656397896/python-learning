m=input()
d=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ','ABCDEFGHIJKLMNOPQRSTUVWXYZ'[::-1]))
x="".join(d.get(c,c) for c in m)
print(x)