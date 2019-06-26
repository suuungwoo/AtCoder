def solve():
    N = int(input())
    pt, px, py = 0, 0, 0
    for i in range(N):
        t, x, y = map(int, input().split())
        dt = abs(t-pt)
        dx = abs(x-px)
        dy = abs(y-py)
        if dx+dy > dt:
            return False
        if (dx+dy) % 2 != dt % 2:
            return False
        pt, px, py = t, x, y
    return True


print(['No', 'Yes'][solve()])
