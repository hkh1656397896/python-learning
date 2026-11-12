def average(x):
    score=[]
    for information in liststudent:
        sum1=information[x]
        score.append(sum1)
    return sum(score)/total

def failed():
    for information in liststudent:
        if information[2]<60 and information[3]<60:   
            print(f"{information[0]} {information[1]} {information[2]} {information[3]}")

def successful():
    for information in liststudent:
        if round((information[2]+information[3])/2,0)>=90:
            print(f"{information[0]} {information[1]} {information[2]} {information[3]}")

f1=open("class_score.txt")
s=f1.readlines()
f1.close()
del s[0]
total=len(s)
liststudent=[]
for i in s:
    line=i.split()
    information=line[0:2]+[int(x) for x in line[2:4]]
    liststudent.append(information)
math_average=f"{average(2):.1f}"
english_average=f"{average(3):.1f}"
print(f"math aver:{math_average},Eng aver:{english_average}") 
print("Two courses failed:")
failed()
print("aver of two(>=90):")
successful()
