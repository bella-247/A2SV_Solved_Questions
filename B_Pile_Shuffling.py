t = int(input())

for _ in range(t):
    n = int(input())
    piles = [list(map(int, input().split())) for _ in range(n)]

    zeros = 0
    ones = 0

    for pile in piles:
        a, b, c, d = pile

        # excess zeros
        if a > c:
            zeros += a - c

        # excess ones
        if b > d:
            ones += (b - d) + min(a, c)

    print(zeros + ones)
