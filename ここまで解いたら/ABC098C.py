# https://atcoder.jp/contests/abc098/tasks/arc098_a

N = int(input())
S = input()

cnt = S.count('E')
if S[0] == 'E':
    cnt -= 1
ans = cnt
for i in range(1, N):
    if S[i] == 'E':
        cnt -= 1
    if S[i - 1] == 'W':
        cnt += 1
    if cnt < ans:
        ans = cnt
print(ans)
