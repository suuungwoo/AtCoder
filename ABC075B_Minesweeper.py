H, W = (int(i) for i in input().split())
glid = [[i for i in input()] for i in range(H)]


def search(x, y):
    try:
        if glid[x][y] == '#' and x != -1 and y != -1:
            return 1
        else:
            return 0
    except:
        return 0


ans = []
for i in range(H):
    ans.append([0 for _ in range(W)])
    for j in range(W):
        if glid[i][j] == '#':
            ans[i][j] = '#'
        else:
            li = [(i-1, j-1), (i, j-1), (i-1, j), (i+1, j+1),
                  (i, j+1), (i+1, j), (i+1, j-1), (i-1, j+1)]
            for x, y in li:
                ans[i][j] += search(x, y)

for i in range(H):
    for j in range(W):
        print(ans[i][j], end="")
    print()
