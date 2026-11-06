def isRepeated(v):
    for i in v:
        if v.count(i)>1:
            return True
    return False

m=list(map(int,input().split(",")))
print(isRepeated(m))
