# https://atcoder.jp/contests/abc085/tasks/abc085_b

N = int(input())
d = list(map(int, [input() for i in range(N)]))

print(len(set(d)))
