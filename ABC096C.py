# https://atcoder.jp/contests/abc096/tasks/abc096_c

H, W = map(int, input().split())
grid = [[i for i in input()] for i in range(H)]

jud = 'Yes'
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            try:
                if grid[i-1][j] == grid[i][j-1] == grid[i][j+1] == grid[i+1][j] == '.':
                    jud = 'No'
                else:
                    continue
            except Exception:
                break

print(jud)
