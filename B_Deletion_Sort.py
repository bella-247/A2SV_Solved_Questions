import sys

input = sys.stdin.readline


def solution():
    n = int(input().strip())
    nums = list(map(int, input().split()))

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            print(1)
            return

    else:
        print(n)
        return

t = 1
t = int(input().strip())
for _ in range(t):
    solution()
