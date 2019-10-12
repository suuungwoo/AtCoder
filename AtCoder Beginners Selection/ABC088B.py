# https://atcoder.jp/contests/abc088/tasks/abc088_b

N = input()
a = list(map(int, input().split()))
a.sort(reverse=True)
print(sum(a[0::2]) - sum(a[1::2]))
