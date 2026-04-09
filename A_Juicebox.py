from collections import defaultdict, deque, Counter
from email.policy import default
import math
import random
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

rand = random.randint(1, 10000)

def solution(_):
    n, k = read_ints()
    
    boxes = [read_list() for _ in range(k)]
    
    costs = defaultdict(int)
    
    for box in boxes:
        costs[box[0] ^ rand] += box[1]

    sorted_costs = sorted(costs.items(), key=lambda item : item[1], reverse=True)

    total = 0
    
    for i in range(min(n, len(sorted_costs))):
        total += sorted_costs[i][1]
    
    print(total)
    

def main():
    t = 1
    t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()