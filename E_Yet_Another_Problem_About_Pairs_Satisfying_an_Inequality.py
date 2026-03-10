from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools

input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7
def solution():
    n = read_int()
    nums = read_list()
    
    indices = []
    valids = [0] * n
    valid_count = 0
    total = 0
    for index in range(1, n + 1):
        i = index - 1
        
        if nums[i] < index:
            indices.append(i)
            valids[i] = valid_count
            valid_count += 1
        
    for i in indices:
        total += (valids[nums[i]-1])
    print(indices)
    print(valids)
    print(total)


def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()