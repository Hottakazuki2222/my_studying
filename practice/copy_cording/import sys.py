import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

count = 0

#マージソート
for i in range(1,n):
    v = A[i]
    j = i - 1

    while j >= 0 and A[j] > v:
        A[j+1] = A[j]
        j -= 1
        count += 1  #試行回数の加算

    A[j+1] = v

#出力
print(*A)
print(count)