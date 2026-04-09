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
    strings = [input().strip() for _ in range(n)]
    
    first_matches = Counter()
    last_matches = Counter()
    both_matches = Counter()
    
    for s in strings:
        first_matches[s[0]] += 1
        last_matches[s[1]] += 1
        both_matches[s] += 1
        
    total = 0
    
    for s, count in both_matches.items():
        first_count = first_matches[s[0]] - count
        last_count = last_matches[s[1]] - count
        
        total += (first_count * count)
        total += (last_count * count)
    
    print(total // 2)



def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution()

if __name__ == "__main__":
    main()