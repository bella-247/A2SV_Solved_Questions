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
def solution(_):
    lines = []
    max_len = 0
    
    for line in sys.stdin:
        line = line.strip()
        max_len = max(max_len, len(line))
        lines.append(line)
    
    alternating = 0
    
    print("*" * (max_len + 2))
    width = max_len
    
    for line in lines:
        line_len = len(line)
        
        left_space = (width - line_len) // 2

        if (width - line_len) % 2 != 0:
            left_space += alternating
            alternating ^= 1
        
        right_space = width - line_len - left_space

        print("*", end="")
        print(" " * left_space, end="")
        print(line, end="")
        print(" " * right_space, end="")
        print("*")
        
    print("*" * (max_len + 2))





def main():
    t = 1
    # t = int(read_int())
    for _ in range(t):
        solution(_)

if __name__ == "__main__":
    main()