# https://atcoder.jp/contests/abc060/tasks/abc060_b

import sys

A, B, C = map(int, input().split())

for i in range(1, B + 1):
    if (i * A + C) % B == 0:
        print('YES')
        sys.exit()
print('NO')
