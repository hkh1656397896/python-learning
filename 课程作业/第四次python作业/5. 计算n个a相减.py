a, n = input().split()
n = int(n)
s = int(a * n)                 # "5"*6 -> 555555
for i in range(n - 1, 0, -1):
    s -= int(a * i)            # 依次减 "5"*5、"5"*4 …… "5"*1
print(s)
