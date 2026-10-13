N=int(input())
for p in range(2,N//2+1):
    for i in range(2,int(p**0.5)+1):
        if p%i==0:break
    else:
        q=N-p
        for j in range(2,int(q**0.5)+1):
            if q%j==0:break
        else:
            print(f"{N} = {p} + {q}")
            break

   


        

