# import sys
# input = sys.stdin.readline


# def main():
#     N = int(input())
#     A = list(map(int, input().split()))

#     ans = 0
#     if 1 not in A:
#         ans = -1
#     else:
#         current_index = A.index(1)
#         for i in range(2, N + 1):
#             if i not in A[current_index + 1:]:
#                 ans = N - i + 1
#                 break
#             else:
#                 current_index = A[current_index + 1:].index(i) + current_index

#     print(ans)


# if __name__ == "__main__":
#     main()

s = int(input())
t = list(map(int, input().split()))
a = 1
b = 0
for i in range(s):
    if a == t[i]:
        a += 1
    else:
        b += 1
if b == s:
    print(-1)
else:
    print(b)
