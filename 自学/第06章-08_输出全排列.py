import itertools
n=int(input())
L=['1','2','3','4','5','6','7','8','9']
t=L[0:n]
x=["".join(i) for i in itertools.permutations(t)]
print(*x,sep="\n")




