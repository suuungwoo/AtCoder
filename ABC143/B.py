N = int(input())
d = list(map(int, input().split()))

all = sum(d)
ans = 0
for i in range(N):
    all -= d[i]
    ans += d[i] * all

print(ans)
