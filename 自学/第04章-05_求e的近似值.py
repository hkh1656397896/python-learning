m=int(input())
term=1.0
e=0.0
i=0
for _ in range(m+1):
    e+=term
    i+=1
    term/=i
print(f"{e:.8f}")    