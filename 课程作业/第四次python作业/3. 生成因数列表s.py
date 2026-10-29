from math import isqrt

n = int(input())
L = []
for p in range(1, isqrt(n) + 1):
    if n % p == 0:          # 必须判整除：原来缺这一句，n=10 时会凭空塞进 3
        q = n // p
        L.append(p)
        if p != q:
            L.append(q)
print(sorted(L))
