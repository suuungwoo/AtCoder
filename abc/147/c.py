import sys
input = sys.stdin.readline


def main():
    N = int(input())
    evidences = [[] for _ in range(N)]
    for n in range(N):
        A = int(input())
        for _ in range(A):
            x, y = map(int, input().split())
            evidences[n].append((x - 1, y))

    result = 0
    for i in range(1, 2**N):
        consistent = True
        for j in range(N):
            for x, y in evidences[j]:
                if (i >> x) & 1 != y:
                    consistent = False
                    break

                # cnt = 0
                # for y in ys:
                #     if all(y):
                #         cnt += 1
                # print(cnt)


if __name__ == "__main__":
    main()
