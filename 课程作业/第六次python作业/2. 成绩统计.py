f1=open("score1.txt", "r")
s=f1.readlines()
f1.close()
del s[0]
print(f"total:{len(s)}")
grades=[]
chengji=[]
for i in s:
    information=i.split()
    score=information[0:2]+[int(x) for x in information[2:4]]
    grades.append(score)
table=[]
for score in grades:
    sum1=int(score[2]*0.3+score[3]*0.7)
    chengji.append(sum1)
    table.append([score[0],score[1],sum1])
f2=open("score2.txt", "w") 
str1="学号 姓名 总评成绩"
f2.write(str1+"\n")
for score in table:
    str1=f"{score[0]}\t{score[1]}\t{score[2]}\n"
    f2.write(str1+"\n")
f2.close()
cnt_90=cnt_80=cnt_70=cnt_60=cnt_low_60=0
for sum2 in chengji:
    if sum2>90:
        cnt_90+=1
    elif sum2>=80:
        cnt_80+=1
    elif sum2>=70:
        cnt_70+=1
    elif sum2>=60:
        cnt_60+=1
    else:
        cnt_low_60+=1
average=int(sum(chengji)/len(s))
print(f">90:{cnt_90}")
print(f"80-89:{cnt_80}")
print(f"70-79:{cnt_70}")
print(f"60-69:{cnt_60}")
print(f"<60:{cnt_low_60}")
print(f"aver of class:{average}")