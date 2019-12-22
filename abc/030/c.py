import bisect
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
X, Y = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

now = 0
cnt = 0
while True:
    a_index = bisect.bisect_left(A, now)
    if a_index == N:
        print(cnt)
        break
    now = A[a_index] + X
    b_index = bisect.bisect_left(B, now)
    if b_index == M:
        print(cnt)
        break
    now = B[b_index] + Y
    cnt += 1
