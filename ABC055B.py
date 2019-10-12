# https://atcoder.jp/contests/abc055/tasks/abc055_b

import math

N = int(input())
ans = math.factorial(N) % (10**9 + 7)
print(ans)
