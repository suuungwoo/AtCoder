import bisect
N = int(input())
L = [int(i) for i in input().split()]

SL = sorted(L)
ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        right = bisect.bisect_left(SL, SL[i] + SL[j])
        left = j + 1
        ans += right - left

print(ans)
