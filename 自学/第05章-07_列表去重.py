L=eval(input())
l=[]
for i in L:
    if i not in l:
        l.append(i)
print(*l)