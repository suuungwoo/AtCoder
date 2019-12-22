import sys
input = sys.stdin.readline


def main():
    N = int(input())

    ans = 0
    if N % 2:
        ans = 0
    elif N < 10:
        ans = 0
    else:
        ans = N / 8 - 5

    print(ans)


if __name__ == "__main__":
    main()
