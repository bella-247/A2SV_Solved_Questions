n = int(input())
nums_set = set(map(int, input().split()))
for i in range(1, n + 1):
    if i not in nums_set:
        print(i)
        break