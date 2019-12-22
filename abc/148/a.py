import sys
input = sys.stdin.readline


def main():
    A, B = int(input()), int(input())
    choice = [1, 2, 3]
    choice.remove(A)
    choice.remove(B)
    print(choice[0])


if __name__ == "__main__":
    main()
