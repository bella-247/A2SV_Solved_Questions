for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n - 1):
        if (nums[i] - nums[i + 1]) % 2 == 0:
            print("NO")
            break

    else:
        print("YES")
