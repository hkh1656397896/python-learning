m=input()
n=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
L=[]
K=[]
a=m.find('-')
yes=0
if m[-1]!='#':
    print()
else:
    for i,ch in enumerate(m):
        if ch in n:
            yes+=1
            L.append(ch)
            K.append(i)
    if yes==0:
        print(0)
    else:      
        x="".join(L)
        X=int(x,16)
        if a<=int(min(K)) and a>=0:
            print(f"{-X}")
        else:
            print(f"{X}")




