# https://atcoder.jp/contests/abc070/tasks/abc070_b

A, B, C, D = map(int, input().split())


print(min(B, D) - max(A, C) if min(B, D) - max(A, C) > 0 else 0)
