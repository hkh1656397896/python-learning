n=int(input())
m=list(map(int,input().split()))
L=sorted(m)
total=set()
for i in L:
    if i not in total:
        total.add(i)
        print(f"{i}:{m.count(i)}")
    else:continue


