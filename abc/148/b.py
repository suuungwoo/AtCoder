import sys
input = sys.stdin.readline


def main():
    _ = int(input())
    S, T = input().split()

    ans = []
    for s, t in zip(S, T):
        ans.append(s)
        ans.append(t)
    print(''.join(ans))


if __name__ == "__main__":
    main()
