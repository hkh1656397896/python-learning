n=int(input())
N=input().split()
r=max(map(int,N))
R=str(r)
yes=0
L=[]
for i,ch in enumerate(N):
    if R==ch:
        yes+=1
        L.append(i)
if yes!=0:        
    print(r,min(L))    
        


