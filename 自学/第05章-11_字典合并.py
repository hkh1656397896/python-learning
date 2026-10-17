x=eval(input())
y=eval(input())
L={**x,**y}
for a,b in x.items():
    for c,d in y.items():
        if a==c:
            v=b+d
            L[a]=v
def mixedkey(kv):
    if isinstance(kv[0],int):
        return kv[0]
    else:
        return ord(kv[0])
K=dict(sorted(L.items(),key=mixedkey))
S=str(K).replace(" ","").replace("'",'"')
print(S)
