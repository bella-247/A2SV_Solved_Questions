n, m = list(map(int, input().split()))

if n > m or m % n != 0:
    print(-1)

else:
    div = m // n
    count = 0

    while div != 1:
        if div % 2 == 0:
            div //= 2

        elif div % 3 == 0:
            div //= 3
        else:
            break

        count += 1

    print(count if div == 1 else -1)
