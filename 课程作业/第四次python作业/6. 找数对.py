line = input().strip()
if line.startswith("numbers:"):        # 样例输入带前缀，先剥掉，不带也能跑
    line = line[len("numbers:"):]
nums = {int(x) for x in line.split(",") if x.strip() != ""}

L = []
for i in sorted(nums):
    j = 9 - i
    if j in nums and i < j:            # i<j 保证小数在前，也避免 (5,4) 这类反向重复
        L.append((i, j))
print(L)
