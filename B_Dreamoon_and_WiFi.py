from collections import defaultdict, deque, Counter
import math
import sys
import bisect
import itertools
from textwrap import dedent

# sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def print(*args, **kwargs):
    sys.stdout.write(" ".join(map(str, args)) + kwargs.get("end", "\n"))

def read_int(): return int(input().strip())
def read_ints(): return map(int, input().split())
def read_list(): return list(map(int, input().split()))
def yn(res): print("YES" if res else "NO")

inf = float('inf')
MOD = 10**9 + 7
def solution(_):
    main = input().strip()
    target = sum(1 if char == "+" else - 1 for char in main)
    s = input().strip()
    
    successful = 0
    unsuccessful = 0
    
    def backtrack(index, summ):
        nonlocal successful
        nonlocal unsuccessful
        
        if index == len(s):
            if summ == target:
                successful += 1
            else:
                unsuccessful += 1
            return
        
        char = s[index]
        match char:
            case "+":
                backtrack(index + 1, summ + 1)
                
            case "-":
                backtrack(index + 1, summ - 1)
                
            case "?":
                backtrack(index + 1, summ + 1)
                backtrack(index + 1, summ - 1)

    backtrack(0, 0)
    res = successful / (successful + unsuccessful)
    print(f"{res:.12f}")





def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()