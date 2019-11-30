# https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int, input().split())
x, y, z = -1, -1, -1
for i in range(N + 1):
    for j in range(N - i + 1):
        if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y:
            x, y, z = i, j, N - i - j
            break
print(x, y, z)
