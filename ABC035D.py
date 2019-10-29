from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import sys


def input():
    return sys.stdin.readline().strip()


N, M, T = list(map(int, input().split()))
A = list(map(int, input().split()))

a = []
b = []
c = []
for i in range(M):
    ai, bi, ci = list(map(int, input().split()))
    a.append(ai - 1)
    b.append(bi - 1)
    c.append(ci)

graph = csr_matrix((c, (a, b)), shape=(N, N))
dist1 = dijkstra(graph, directed=True, indices=0)
list(dist1)

graph2 = csr_matrix((c, (b, a)), shape=(N, N))
dist2 = dijkstra(graph2, directed=True, indices=0)
list(dist2)

ans = 0

for i in range(N):
    ans = max(ans, A[i] * (T - dist1[i] - dist2[i]))

print(int(ans))
