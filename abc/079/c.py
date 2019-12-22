from itertools import zip_longest
import sys
input = sys.stdin.readline


def main():
    ABCD = list(input().rstrip())
    n = len(ABCD) - 1

    for i in range(2**n):
        op = ['+' if ((i >> j) & 1) else '-' for j in range(n)]
        cal = ''.join([i + j for i, j in zip_longest(ABCD, op, fillvalue='')])
        if eval(cal) == 7:
            print(cal + '=7')
            break


if __name__ == "__main__":
    main()
