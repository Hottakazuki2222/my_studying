import sys

# 入力
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

count = 0

# 挿入ソート
for i in range(1, n):
    v = A[i]
    j = i - 1

    while j >= 0 and A[j] > v:
        A[j + 1] = A[j]
        j -= 1
        count += 1   # ← 移動回数をカウント

    A[j + 1] = v

# 出力
print(*A)
print(count)