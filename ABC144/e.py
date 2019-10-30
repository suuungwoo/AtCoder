import numpy as np
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = np.sort(list(map(int, input().split())))
F = np.sort(list(map(int, input().split())))[::-1]

t_max = A[-1] * F[0]
t_min = -1

while t_max > t_min + 1:
    t_mid = (t_max + t_min) // 2
    K_tmp = np.sum(np.maximum(A - t_mid // F, 0))
    if K_tmp <= K:
        t_max = t_mid
    else:
        t_min = t_mid

print(t_max)
