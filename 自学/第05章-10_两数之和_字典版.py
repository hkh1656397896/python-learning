total=list(map(int,input().split(',')))
m=int(input())
d={}
for i,ch in enumerate(total):
    n=m-ch
    if n in d:
        print(d[n],i)
        break
    d[ch]=i
else:
    print('no answer')
