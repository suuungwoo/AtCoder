# https://atcoder.jp/contests/abc087/tasks/arc090_a

N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

ans = 0
for i in range(N):
    candies = 0
    for j in range(i + 1):
        candies += A1[j]
    for k in range(i, N):
        candies += A2[k]
    if candies > ans:
        ans = candies

print(ans)
