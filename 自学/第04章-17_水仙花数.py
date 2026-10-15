m=int(input())
L=[]
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    if m==3:
                        total=a*100+b*10+c
                        if a**3+b**3+c**3==total and total not in L:
                            L.append(total)
                            print(total,sep='\n')
                    elif m==4:
                        total=a*1000+b*100+c*10+d
                        if a**4+b**4+c**4+d**4==total and total not in L:
                            L.append(total)
                            print(total,sep='\n')
                    else:
                        total=a*10000+b*1000+c*100+d*10+e
                        if a**5+b**5+c**5+d**5+e**5==total and total not in L:
                            L.append(total)
                            print(total,sep='\n')
