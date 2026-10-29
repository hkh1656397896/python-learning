m, n = map(int, input().split(","))
cnt = 0
for i in range(m, n + 1):
    if i < 2:          # 1 和 0 不是质数，必须跳过，否则 for-else 会把它们当质数
        continue
    for z in range(2, int(i ** 0.5) + 1):
        if i % z == 0:
            break
    else:
        cnt += 1
        print(f"{i:<5}", end="")
        if cnt % 5 == 0:   # 换行要放这里：每输出 5 个质数才换行
            print()
if cnt == 0:
    print(0)
