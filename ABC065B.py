# https://atcoder.jp/contests/abc065/tasks/abc065_b

N = int(input())
a = list(map(int, [input() for i in range(N)]))

current_index = 1
for i in range(N - 1):
    current_index = a[current_index - 1]
    if current_index == 2:
        print(i + 1)
        exit()

print(-1)
