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
    a = read_list()
    b = read_list()
    
    a.sort(reverse=True)
    b = list(itertools.accumulate(b))
    
    largest = 0
    levels_passed = 0
    
    for i, x in enumerate(a):
        swords_count = i + 1
        
        j = levels_passed
        while j < n and swords_count >= b[j]:
            levels_passed += 1
            j += 1
        
        largest = max(largest, x * levels_passed)

    print(largest)
        





def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()