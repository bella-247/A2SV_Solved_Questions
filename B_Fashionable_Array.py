from collections import Counter

for _ in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))
    counts = Counter(nums)
    distinct = sorted(set(nums), reverse=True)

    result = []

    while len(result) < n:
        for num in distinct:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

    print(*result)
    