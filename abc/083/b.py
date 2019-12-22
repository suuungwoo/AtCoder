import sys
input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())
    ans = 0

    # 線形探索（O(n))
    # for n in range(N + 1):
    #     if A <= sum(list(map(int, str(n)))) <= B:
    #         ans += n

    # bit探索(O(log n))
    for i in range(N + 1):
        each_digits_total = 0
        j = i
        while j > 0:
            each_digits_total += j % 10
            j //= 10
        if A <= each_digits_total <= B:
            ans += i
    print(ans)


if __name__ == "__main__":
    main()
