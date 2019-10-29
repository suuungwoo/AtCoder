N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


divisors = make_divisors(N)
if len(divisors) % 2 == 0:
    print(divisors[int(len(divisors) // 2)] +
          divisors[int(len(divisors) // 2) - 1] - 2)
else:
    print(divisors[int(len(divisors) // 2)] * 2 - 2)
